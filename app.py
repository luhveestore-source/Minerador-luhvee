import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import requests
from bs4 import BeautifulSoup

# Configuração da Página
st.set_page_config(page_title="Minerador Viral Pro", layout="wide")

st.title("🚀 Minerador de Produtos Virais - Nível Brasil")
st.subheader("Encontre tendências para Dropshipping e Marketplace")

# Sidebar para Filtros
st.sidebar.header("Configurações de Mineração")
categoria = st.sidebar.text_input("Palavra-chave (ex: Cozinha, Pet, Tech)", "Ofertas")

def buscar_google_trends(termo):
    try:
        pytrends = TrendReq(hl='pt-BR', tz=360)
        pytrends.build_payload([termo], geo='BR', timeframe='now 7-d')
        df = pytrends.related_queries()
        return df[termo]['top']
    except:
        return pd.DataFrame({"Erro": ["Muitas requisições, tente novamente em instantes."]})

def buscar_mercado_livre(termo):
    url = f"https://lista.mercadolivre.com.br/{termo}#D[A:{termo}]"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    produtos = []
    itens = soup.find_all('div', class_='ui-search-result__content-wrapper', limit=10)
    
    for item in itens:
        try:
            nome = item.find('h2').text
            preco = item.find('span', class_='andes-money-amount__fraction').text
            link = item.find('a')['href']
            produtos.append({"Produto": nome, "Preço (R$)": preco, "Link": link})
        except:
            continue
    return pd.DataFrame(produtos)

# Botão de Ação
if st.button("🔍 Minerar Tendências Agora"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🔥 Termos em Alta (Google Brasil)")
        dados_google = buscar_google_trends(categoria)
        st.dataframe(dados_google)
        
    with col2:
        st.write("### 🛒 Mais Vendidos (Mercado Livre)")
        dados_ml = buscar_mercado_livre(categoria)
        st.table(dados_ml)

    st.success("Mineração concluída em tempo real!")
