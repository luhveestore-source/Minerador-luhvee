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
