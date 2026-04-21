import cloudscraper
from bs4 import BeautifulSoup
import random
import time

scraper = cloudscraper.create_scraper()

def buscar_ml(keyword):
    url = f"https://lista.mercadolivre.com.br/{keyword}"

    try:
        r = scraper.get(url, timeout=10)
    except:
        return []

    soup = BeautifulSoup(r.text, "lxml")

    produtos = []

    items = soup.find_all("li", class_="ui-search-layout__item")

    for item in items[:20]:
        try:
            titulo = item.find("h2").text.strip()
            preco_tag = item.find("span", class_="andes-money-amount__fraction")

            if not preco_tag:
                continue

            preco = int(preco_tag.text.replace(".", ""))
            link = item.find("a")["href"]

            produtos.append({
                "titulo": titulo,
                "preco": preco,
                "link": link,
                "plataforma": "Mercado Livre"
            })
        except:
            continue

    return produtos


def score_viral(produto):
    score = 0

    if produto["preco"] < 150:
        score += 30

    palavras = ["oferta", "promo", "kit", "original", "frete grátis"]
    for p in palavras:
        if p in produto["titulo"].lower():
            score += 20

    score += random.randint(20, 50)

    return score


def detectar_publico(titulo):
    t = titulo.lower()

    if "pele" in t or "anti" in t:
        return "Mulheres 25-45 (Beleza)"

    if "smart" in t:
        return "Homens 18-35 (Tech)"

    if "cozinha" in t:
        return "Famílias / Casa"

    return "Público geral"


def minerar():
    palavras = [
        "air fryer",
        "smartwatch",
        "escova secadora",
        "creme facial",
        "emagrecedor"
    ]

    resultados = []

    for p in palavras:
        produtos = buscar_ml(p)

        if not produtos:
            print(f"⚠️ Nada encontrado para: {p}")
            continue

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
