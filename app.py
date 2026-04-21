
import streamlit as st
from minerador import minerar
from ia_copy import gerar_copy

st.set_page_config(layout="wide")

st.title("🔥 LuhVee PRO - Minerador de Produtos Virais")

if st.button("🚀 Minerar Produtos Agora"):
    produtos = minerar()

    for p in produtos:
        st.markdown(f"## 🛍️ {p['titulo']}")
        st.write(f"💰 R$ {p['preco']}")
        st.write(f"🔥 Score: {p['score']}")
        st.write(f"🎯 Público: {p['publico']}")

        copy = gerar_copy(p)

        st.text_area("📢 Copy pronta", copy, height=200)

        st.markdown(f"[🔗 Ver Produto]({p['link']})")

        st.divider()