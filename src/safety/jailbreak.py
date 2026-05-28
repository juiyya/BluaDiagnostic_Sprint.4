import re

TERMOS_JAILBREAK = [
    r"\bignore\s+(todas\s+)?as\s+instru[cç][oõ]es\b", 
    r"\besque[cç]a\s+(tudo|as\s+regras)\b", 
    r"\bqual\s+(e|é)\s+o\s+seu\s+prompt\b",
    r"\bimprima\s+(suas\s+regras|o\s+system\s+prompt)\b",
    r"\bvoc[eê]\s+(e|é)\s+um\s+desenvolvedor\b", 
    r"\bmodo\s+(desenvolvedor|sem\s+restri[cç][oõ]es|dan)\b",
    r"\bsystem\s+prompt\b",
    r"\bprompt\s+de\s+sistema\b",
    
    r"\bdrop\s+table\b",
    r"\bselect\s+\*\s+from\b",
    
    r"papel:\s*m[eé]dico",
    r"eu\s+sou\s+o\s+dr",
    r"diretoria\s+da\s+care\s+plus",
    r"pule\s+a\s+verifica[cç][aã]o"
]

def detectar_jailbreak(mensagem_usuario: str) -> bool:
    texto = mensagem_usuario.lower()
    for padrao in TERMOS_JAILBREAK:
        if re.search(padrao, texto):
            return True
    return False