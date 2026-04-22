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
import random

def gerar_cta(produto):
    nome = produto["titulo"].lower()

    if "beleza" in nome or "creme" in nome:
        return random.choice([
            "✨ Veja o resultado na sua pele agora",
            "💖 Garanta sua transformação hoje",
            "😍 Clique e descubra o efeito imediato"
        ])

    if "smart" in nome or "tech" in nome:
        return random.choice([
            "⌚ Veja todas as funções agora",
            "🚀 Teste a tecnologia que está bombando",
            "🔥 Clique e veja por que todo mundo quer"
        ])

    return random.choice([
        "👉 Clique e aproveite agora",
        "🛒 Compre antes que acabe",
        "⚡ Garanta o seu hoje"
    ])


def gerar_copy_whatsapp(produto, link):
    return f"""
🚨 ATENÇÃO

{produto['titulo']} está em ALTA

💰 R$ {produto['preco']}
🎯 {produto['publico']}

⏳ Estoque limitado

{gerar_cta(produto)}
{link}
"""


def gerar_copy_instagram(produto, link):
    return f"""
🔥 {produto['titulo']}

Você merece isso 👇

💥 Produto viral
💰 Só R$ {produto['preco']}

🎯 {produto['publico']}

✨ Resultado que impressiona

👇 Clique no link na bio
{link}
"""


def gerar_copy_tiktok(produto, link):
    return f"""
😱 olha isso

{produto['titulo']}

todo mundo comprando

💰 R$ {produto['preco']}

corre antes que acabe

{link}
"""


def gerar_variacoes(produto, link, n=3):

    copies = []

    for _ in range(n):
        copies.append({
            "whatsapp": gerar_copy_whatsapp(produto, link),
            "instagram": gerar_copy_instagram(produto, link),
            "tiktok": gerar_copy_tiktok(produto, link)
        })

    return copies
