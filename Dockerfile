FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# VARIÁVEL DE REDE: Aponta para o Ollama na máquina hospedeira. 
# isso não é uma API Key, é apenas uma rota local segura.
ENV OLLAMA_BASE_URL="http://host.docker.internal:11434"

# porta padrão do Streamlit
EXPOSE 8501

# Verifica se a interface subiu corretamente
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# inicialização, amarrando o IP 0.0.0.0 para acesso externo
ENTRYPOINT ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]