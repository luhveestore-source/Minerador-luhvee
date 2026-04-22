import random

def gerar_copy(produto, link):

    hooks = [
        f"🚨 {produto['titulo']} está ESGOTANDO rápido!",
        f"😱 Ninguém te contou isso sobre {produto['titulo']}",
        f"🔥 O produto mais comprado do momento",
        f"⚠️ Se você viu isso, aproveite agora"
    ]

    dores = [
        "Cansado de produtos que não funcionam?",
        "Chega de gastar dinheiro à toa.",
        "Se você quer resultado de verdade, presta atenção nisso.",
        "A maioria das pessoas erra aqui..."
    ]

    provas = [
        "💥 Viral no TikTok",
        "🔥 Milhares de pessoas já compraram",
        "🚀 Sucesso nos EUA",
        "⭐ Altamente avaliado"
    ]

    urgencia = [
        "⏳ Últimas unidades disponíveis",
        "⚠️ Pode acabar a qualquer momento",
        "🔥 Alta demanda HOJE",
        "🚨 Promoção por tempo limitado"
    ]

    ctas = [
        "👉 Clique e garanta agora",
        "🛒 Compre antes que acabe",
        "🔥 Aproveite enquanto ainda tem",
        "👇 Toque aqui e veja a oferta"
    ]

    return f"""
{random.choice(hooks)}

{random.choice(dores)}

🛍️ {produto['titulo']}

💰 De R$ {produto['preco']*2} por apenas R$ {produto['preco']}

{random.choice(provas)}

🎯 Ideal para: {produto['publico']}

{random.choice(urgencia)}

{random.choice(ctas)}
{link}
"""
