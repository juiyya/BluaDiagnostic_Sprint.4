import os
from observability.logger import logger

def inicializar_tracing():

    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        logger.info(" [tracing] LangSmith Tracing detectado e ativado.")
    else:
        logger.info(" [tracing] Executando com telemetria local por console.")