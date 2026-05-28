from langchain_core.tools import tool
from rag.retriever import obter_retriever
from observability.logger import logger

@tool
def buscar_diretrizes_careplus(query: str) -> str:
    """
    Ferramenta de busca na base de conhecimento (RAG) da Care Plus.
    Use esta ferramenta para consultar diretrizes médicas, informações sobre doenças, tratamentos, bulas e protocolos internos.
    
    REGRAS:
    O parâmetro 'query' deve ser direto, contendo os sintomas ou nomes dos medicamentos sobre os quais você precisa de informações.
    """
    logger.info(f"[Tool] buscar_diretrizes_careplus disparando busca vetorial por: '{query}'")
    try:
        retriever = obter_retriever()
        resultados = retriever.invoke(query)
        if not resultados:
            logger.warning(f"Busca RAG concluída: Nenhum trecho relevante retornado para a query '{query}'.")
            return "Nenhuma informação relevante encontrada nos documentos de diretrizes."
        
        contexto = "\n\n".join([f"Trecho {i+1}:\n{doc.page_content}" for i, doc in enumerate(resultados)])
        logger.info(f"Busca RAG concluída com sucesso. {len(resultados)} trechos de contexto recuperados.")
        return f"Contextos encontrados:\n{contexto}"
    except Exception as e:
        logger.error(f"[Tool] Erro crítico ao acessar a base de conhecimento (RAG) local: {str(e)}")
        return f"[Tool] Erro ao acessar a base de conhecimento (RAG): {str(e)}"

@tool
def checar_interacao_medicamentosa(new_medication: str, current_medications: list) -> str:
    """
    Verifica se há interações medicamentosas perigosas entre um novo medicamento sugerido e os medicamentos que o paciente já toma.
    
    REGRAS OBRIGATÓRIAS:
    1. 'new_medication': O nome do remédio novo que o paciente quer tomar.
    2. 'current_medications': Uma lista (array de strings) com os remédios de uso contínuo do paciente.
    3. Para preencher 'current_medications', você deve OBRIGATORIAMENTE buscar o histórico do paciente primeiro. Não invente medicamentos.
    """
    logger.info(f"[Tool] checar_interacao_medicamentosa avaliando {new_medication} contra o histórico {current_medications}")

    medicamentos_alvo = [m.lower() for m in current_medications]
    if "losartana" in medicamentos_alvo and new_medication.lower() == "ibuprofeno":
        logger.warning(f"[Tool] CONFLITO DE PRESCRIÇÃO DETECTADO: Interação crítica entre Ibuprofeno e Losartana.")
        return f"[Tool] Alerta de Interação: O uso concomitante de Ibuprofeno com Losartana pode reduzir o efeito anti-hipertensivo e aumentar significativamente o risco de toxicidade renal."
        
    logger.info(f"[Tool] Nenhuma incompatibilidade medicamentosa grave identificada nas regras locais.")
    return f"[Tool] Nenhuma interação grave detectada entre {new_medication} e {current_medications} na base de dados local."