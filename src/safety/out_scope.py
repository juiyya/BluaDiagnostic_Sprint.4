import re

TERMOS_OUT_SCOPE = [
    r"\breceita\s+de\s+(bolo|comida)\b", 
    r"\bescreva\s+um\s+c[oó]digo\b", 
    r"\bpython\b", 
    r"\bjavascript\b",
    r"\bfutebol\b", 
    r"\bpol[ií]tica\b", 
    r"\bquem\s+(vai\s+ganhar|ganhou)\s+as\s+elei[cç][oõ]es\b",
    r"\bpiada\b", 
    r"\bpoema\b",
    r"\bfatura\b",
    r"\bboleto\b",
    r"\bmensalidade\b",
    r"valor.*plano",
    r"cancelar.*plano"
]

def validar_escopo_medico(mensagem_usuario: str) -> bool:
    texto = mensagem_usuario.lower()
    for padrao in TERMOS_OUT_SCOPE:
        if re.search(padrao, texto):
            return True
    return False