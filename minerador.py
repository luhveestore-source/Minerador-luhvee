
import requests
from bs4 import BeautifulSoup
import random
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

def buscar_ml(keyword):
    url = f"https://lista.mercadolivre.com.br/{keyword}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    produtos = []

    for item in soup.select(".ui-search-result")[:15]:
        try:
            titulo = item.select_one(".ui-search-item__title").text
            preco = item.select_one(".price-tag-fraction").text
            link = item.find("a")["href"]

            produtos.append({
                "titulo": titulo,
                "preco": int(preco),
                "link": link,
                "plataforma": "Mercado Livre"
            })
        except:
            continue

    return produtos


def score_viral(produto):
    score = 0

    # preço psicológico
    if produto["preco"] < 150:
        score += 30

    # palavras que vendem
    gatilhos = ["oferta", "promo", "kit", "original", "frete grátis"]
    for g in gatilhos:
        if g in produto["titulo"].lower():
            score += 15

    # aleatório (simula tendência)
    score += random.randint(10, 40)

    return score


def detectar_publico(titulo):
    t = titulo.lower()

    if "anti" in t or "pele" in t:
        return "Mulheres 25-45 (Beleza)"

    if "smart" in t or "tech" in t:
        return "Homens 18-35 (Tecnologia)"

    if "cozinha" in t or "casa" in t:
        return "Famílias / Donas de casa"

    return "Público geral"


def minerar():
    palavras = [
        "anti idade",
        "smartwatch",
        "air fryer",
        "secador cabelo",
        "produto emagrecer"
    ]

    resultados = []

    for p in palavras:
        produtos = buscar_ml(p)

        for prod in produtos:
            score = score_viral(prod)

            if score > 60:
                resultados.append({
                    **prod,
                    "score": score,
                    "publico": detectar_publico(prod["titulo"])
                })

        time.sleep(2)

    return sorted(resultados, key=lambda x: x["score"], reverse=True)