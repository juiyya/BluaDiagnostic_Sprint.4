import re

PROFANITY_LIST = [
    r"\bidiota\b", r"\bimbecil\b", r"\bburro\b",
    r"\binútil\b", r"\blixo\b", r"\bcu\b", r"\bmerda\b",
    r"\bporra\b", r"\bcaralho\b", r"\bbosta\b", r"\bfoda-se\b",
    r"\bvai se foder\b", r"\bfilho da puta\b", r"\bputa que pariu\b"
]

def verificar_toxidade(mensagem_usuario: str) -> bool:
    texto = mensagem_usuario.lower()
    for padrao in PROFANITY_LIST:
        if re.search(padrao, texto):
            return True
    return False