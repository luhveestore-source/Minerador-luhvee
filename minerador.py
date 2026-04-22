import random

def minerar():
    produtos = [
        ("Escova Secadora Profissional", 129),
        ("Smartwatch Ultra 8", 189),
        ("Cinta Modeladora Redutora", 79),
        ("Creme Anti Idade Premium", 97),
        ("Mini Projetor Portátil", 220),
        ("Air Fryer Digital 4L", 299),
    ]

    lista = []

    for nome, preco in produtos:
        lista.append({
            "titulo": nome,
            "preco": preco,
            "score": random.randint(80, 100),
            "publico": detectar_publico(nome)
        })

    return lista


def detectar_publico(nome):
    nome = nome.lower()

    if "creme" in nome:
        return "Mulheres 25-45"

    if "smart" in nome:
        return "Homens 18-35"

    if "cinta" in nome:
        return "Mulheres estética"

    return "Público geral"
