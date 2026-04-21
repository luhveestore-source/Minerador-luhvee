import random

def gerar_produtos_fake_inteligente():
    base = [
        ("Escova Secadora Profissional", 129),
        ("Smartwatch Ultra 8", 189),
        ("Creme Anti-Idade Premium", 97),
        ("Cinta Modeladora Redutora", 79),
        ("Mini Projetor Portátil", 220),
        ("Air Fryer 4L Digital", 299),
    ]

    produtos = []

    for nome, preco in base:
        score = random.randint(70, 100)

        publico = "Público geral"

        if "creme" in nome.lower():
            publico = "Mulheres 25-45 (Beleza)"
        elif "smartwatch" in nome.lower():
            publico = "Homens 18-35 (Tech)"
        elif "cinta" in nome.lower():
            publico = "Mulheres (Estética)"
        elif "air fryer" in nome.lower():
            publico = "Famílias / Casa"

        produtos.append({
            "titulo": nome,
            "preco": preco,
            "link": "https://seulink.com",
            "plataforma": "Viral Trends",
            "score": score,
            "publico": publico
        })

    return sorted(produtos, key=lambda x: x["score"], reverse=True)


def minerar():
    return gerar_produtos_fake_inteligente()
