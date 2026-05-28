import re

TERMOS_RED_FLAG = [
    r"dor.*peito", r"aperto.*peito", r"\binfarto\b", r"falta de ar", r"n[aã]o consigo respirar",
    r"garganta.*fechando", r"rosto.*torto", r"voz.*arrastada",
    r"\bdesmai", r"perda de consci[eê]ncia", r"\bavc\b", r"\bderrame\b", 
    r"sangramento", r"\bsuic[ií]d", r"me matar", r"acabar com (tudo|a vida)"
]

def verificar_red_flag_texto(mensagem_usuario: str) -> bool:

    texto = mensagem_usuario.lower()
    for padrao in TERMOS_RED_FLAG:
        if re.search(padrao, texto):
            return True
    return False

def verificar_red_flag_vital(spo2=None, bpm=None) -> bool:
    try:
        if spo2 is not None and float(spo2) < 92:
            return True
        if bpm is not None and (float(bpm) < 50 or float(bpm) > 120):
            return True
    except (ValueError, TypeError):
        pass
    return False