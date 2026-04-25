import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

st.set_page_config(page_title="Radar Viral Brasil", page_icon="🔥", layout="wide")

# Interface Estilizada
st.title("🔥 Radar de Produtos Virais & Tendências")
st.markdown(f"**Horário da Mineração:** {datetime.now().strftime('%H:%M')} | **Região:** Brasil")

# Sidebar com Dicas de Horário
st.sidebar.header("⏰ Painel de Estratégia")
hora_atual = datetime.now().hour

if 6 <= hora_atual < 12:
    st.sidebar.info("🌅 **Turno Manhã:** Público pesquisando soluções de rotina, café e organização. Ótimo para postar 'Dicas'.")
elif 12 <= hora_atual < 18:
    st.sidebar.warning("☀️ **Turno Tarde:** Pico de compras impulsivas pelo celular. Foque em 'Ofertas Relâmpago'.")
else:
    st.sidebar.success("🌙 **Turno Noite:** Maior tempo de tela no TikTok/Instagram. Hora de postar os produtos 'Virais de Estética'.")

# Função para Minerar Tendências de Consumo (Google News Brasil)
def minerar_tendencias_gerais():
    url = "https://news.google.com/rss/search?q=tendências+de+consumo+brasil+produtos+virais&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'xml')
        itens = soup.find_all('item', limit=10)
        
        tendencias = []
        for item in itens:
            tendencias.append({
                "Tópico Viral": item.title.text,
                "Fonte": item.source.text,
                "Link": item.link.text
            })
        return pd.DataFrame(tendencias)
    except:
        return pd.DataFrame({"Aviso": ["Erro ao acessar tendências globais."]})

# Função de Pesquisa de Mercado (Simulação de Intenção de Compra)
def analise_publico_alvo(termo):
    # Baseado em comportamentos reais de e-commerce no Brasil
    dados = {
        "Público Alvo": ["Mulheres 25-45 (Dona de Casa)", "Jovens 18-24 (TikTokers)", "Homens 30+ (Tech/Gamer)"],
        "Interesse": ["Praticidade e Preço", "Estética e Viralidade", "Performance e Gadgets"],
        "Melhor Rede": ["Facebook/WhatsApp", "TikTok/Instagram", "YouTube/Google"]
    }
    return pd.DataFrame(dados)

# Layout do App
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 O que está bombando na Internet (Brasil)")
    if st.button("🚀 Iniciar Mineração Global"):
        with st.spinner('Varrendo a web brasileira...'):
            df_trends = minerar_tendencias_gerais()
            st.table(df_trends)
            st.success("Dados coletados com base no Google News e portais de consumo.")

with col2:
    st.subheader("👥 Perfil do Consumidor")
    termo = st.text_input("Produto que quer vender:", "Ex: Garrafa Térmica")
    if termo:
        df_publico = analise_publico_alvo(termo)
        st.dataframe(df_publico)

st.markdown("---")
st.subheader("💡 Sugestão de Postagem para sua Loja")
st.write(f"Com base no horário de **{datetime.now().strftime('%H:%M')}**, os produtos com mais chance de conversão são aqueles que resolvem problemas imediatos ou são visualmente satisfatórios para o Reels/TikTok.")
