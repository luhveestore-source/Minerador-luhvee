import streamlit as st
from minerador import minerar
from ia_copy import gerar_copy
from afiliados import gerar_link

st.set_page_config(layout="wide")

st.title("🔥 LuhVee Sistema Automático de Vendas")

if st.button("🚀 GERAR PRODUTOS PARA VENDER"):
    
    produtos = minerar()

    for p in produtos:

        link = gerar_link(p["titulo"])
        copy = gerar_copy(p, link)

        st.markdown(f"## 🛍️ {p['titulo']}")
        st.write(f"💰 R$ {p['preco']}")
        st.write(f"🎯 Público: {p['publico']}")

        st.text_area("📢 COPY PRONTA", copy, height=200)

        st.markdown(f"[🔗 LINK DE VENDA]({link})")

        st.divider()
