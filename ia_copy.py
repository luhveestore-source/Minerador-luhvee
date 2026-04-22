import random

def gerar_copy(produto, link):

    gatilhos = [
        "🔥 ESTOQUE ACABANDO",
        "🚨 TODO MUNDO COMPRANDO",
        "⚠️ ÚLTIMAS UNIDADES",
        "💥 VIRAL NO TIKTOK"
    ]

    return f"""
{random.choice(gatilhos)}

🛍️ {produto['titulo']}

💰 Apenas R$ {produto['preco']}
🎯 Ideal para: {produto['publico']}

👉 GARANTA AGORA:
{link}
"""
