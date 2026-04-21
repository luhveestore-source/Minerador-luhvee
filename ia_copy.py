
import random

def gerar_copy(produto):
    headlines = [
        f"🔥 {produto['titulo']} está explodindo de vendas!",
        f"🚨 Todo mundo está comprando isso AGORA",
        f"😱 Você não vai acreditar nesse produto"
    ]

    gatilhos = [
        "estoque quase esgotado",
        "últimas unidades",
        "sucesso nos EUA",
        "viral no TikTok"
    ]

    headline = random.choice(headlines)
    gatilho = random.choice(gatilhos)

    texto = f"""
{headline}

💥 {gatilho}
💰 Apenas R$ {produto['preco']}
🎯 Perfeito para: {produto['publico']}

👉 Clique agora antes que acabe:
{produto['link']}
"""

    return texto