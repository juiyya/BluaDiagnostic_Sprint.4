from langgraph import graph
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from graph.state import State
from graph.routing import roteamento_supervisor
from agents.supervisor_agent import supervisor_node
from agents.triage_agent import triage_node, triage_tools
from agents.prescription_agent import prescription_node, prescription_tools
from agents.escalation_agent import escalation_node, escalation_tools
from agents.schedule_agent import schedule_node, scheduling_tools

def build_graph():
    graph_builder = StateGraph(State)
    
    # Agentes
    graph_builder.add_node("supervisor_agent", supervisor_node)
    graph_builder.add_node("triage_agent", triage_node)
    graph_builder.add_node("prescription_agent", prescription_node)
    graph_builder.add_node("escalation_agent", escalation_node)
    graph_builder.add_node("schedule_agent", schedule_node)
    
    # TOOLS
    graph_builder.add_node("triage_tools", ToolNode(triage_tools))
    graph_builder.add_node("prescription_tools", ToolNode(prescription_tools))
    graph_builder.add_node("escalation_tools", ToolNode(escalation_tools))
    graph_builder.add_node("scheduling_tools", ToolNode(scheduling_tools))
    
    # SUPERVISOR
    graph_builder.add_edge(START, "supervisor_agent")
    graph_builder.add_conditional_edges("supervisor_agent", roteamento_supervisor)
    
    # triage_agent
    graph_builder.add_conditional_edges("triage_agent", tools_condition, {"tools": "triage_tools", END: END})
    graph_builder.add_edge("triage_tools", "triage_agent")
    
    # prescription_agent
    graph_builder.add_conditional_edges("prescription_agent", tools_condition, {"tools": "prescription_tools", END: END})
    graph_builder.add_edge("prescription_tools", "prescription_agent")
    
    # escalation_agent
    graph_builder.add_conditional_edges("escalation_agent", tools_condition, {"tools": "escalation_tools", END: END})
    graph_builder.add_edge("escalation_tools", "escalation_agent")

    # schedule_agent
    graph_builder.add_conditional_edges("schedule_agent", tools_condition, {"tools": "scheduling_tools", END: END})
    graph_builder.add_edge("scheduling_tools", "schedule_agent")

    memoria = MemorySaver()
    return graph_builder.compile(checkpointer=memoria)