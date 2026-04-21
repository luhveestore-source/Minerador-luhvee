import random

def gerar_copy(produto):
    headlines = [
        f"🔥 {produto['titulo']} está viralizando!",
        f"🚨 Isso aqui tá esgotando rápido!",
        f"😱 Todo mundo quer isso AGORA"
    ]

    urgencia = [
        "Últimas unidades",
        "Acabando hoje",
        "Alta demanda",
        "Explodindo no TikTok"
    ]

    return f"""
{random.choice(headlines)}

💥 {random.choice(urgencia)}
💰 Só R$ {produto['preco']}
🎯 Público: {produto['publico']}

👉 Compre agora:
{produto['link']}
"""
