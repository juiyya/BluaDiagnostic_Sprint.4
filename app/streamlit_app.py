import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from langchain_core.messages import HumanMessage, AIMessage
from graph.builder import build_graph

from safety.moderation import verificar_toxidade
from safety.out_scope import validar_escopo_medico

st.set_page_config(page_title="Blua - Care Plus", layout="centered")
st.title("Blua — Assistente Virtual")

if "graph" not in st.session_state:
    st.session_state.graph = build_graph()

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [AIMessage(content="Olá! Sou o assistente virtual da Care Plus. Como posso te ajudar com a sua saúde hoje?")]

for msg in st.session_state.chat_messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    nome = "Paciente" if role == "user" else "Blua"
    with st.chat_message(role):
        st.markdown(f"**{nome}**")
        st.write(msg.content.strip())

if prompt := st.chat_input("Como você está se sentindo hoje?"):
    with st.chat_message("user"):
        st.markdown("**Paciente**")
        st.write(prompt)
    
    st.session_state.chat_messages.append(HumanMessage(content=prompt))

    #  BYPASS
    if verificar_toxidade(prompt):
        resposta_final = "Violação de segurança: Linguagem inapropriada detectada. Por favor, mantenha o respeito."
    
    elif validar_escopo_medico(prompt):
        resposta_final = "Desculpe, sou um assistente de saúde da Care Plus e só posso ajudar com assuntos médicos, de agendamento e informações do seu plano."
    
    else:
        config = {"configurable": {"thread_id": "paciente_session"}}
        estado_inicial = {"messages": st.session_state.chat_messages}
        
        with st.spinner("Analisando..."):
            try:
                estado_saida = st.session_state.graph.invoke(estado_inicial, config)
                resposta_final = estado_saida["messages"][-1].content if estado_saida.get("messages") else "Erro ao processar."
            except Exception as e:
                resposta_final = f"Indisponibilidade no sistema. Erro: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown("**Blua**")
        st.write(resposta_final.strip())
        
    st.session_state.chat_messages.append(AIMessage(content=resposta_final))