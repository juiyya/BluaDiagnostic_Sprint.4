import os

def carregar_prompt(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), '..', 'prompts', nome_arquivo)
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()