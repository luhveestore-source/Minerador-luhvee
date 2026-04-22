import streamlit as st
from minerador import minerar
from afiliados import gerar_link
from ia_copy import gerar_variacoes

st.set_page_config(layout="wide")

st.title("🔥 LuhVee Sistema Automático de Vendas")

st.markdown("Gere produtos + copies prontas para vender em todas as plataformas")

if st.button("🚀 GERAR PRODUTOS AGORA"):

    with st.spinner("Gerando produtos virais..."):
        produtos = minerar()

    if not produtos:
        st.error("⚠️ Nenhum produto encontrado")
    else:
        for p in produtos:

            link = gerar_link(p["titulo"])

            st.markdown(f"## 🛍️ {p['titulo']}")
            st.write(f"💰 Preço: R$ {p['preco']}")
            st.write(f"🎯 Público: {p['publico']}")
            st.write(f"🔥 Score: {p['score']}")

            st.markdown(f"[🔗 LINK DE VENDA]({link})")

            st.markdown("### 🤖 Copies prontas para postar")

            variacoes = gerar_variacoes(p, link, 2)

            for i, v in enumerate(variacoes):

                st.markdown(f"### 🔥 Variação {i+1}")

                st.text_area(
                    f"WhatsApp {i}",
                    v["whatsapp"],
                    height=150
                )

                st.text_area(
                    f"Instagram {i}",
                    v["instagram"],
                    height=150
                )

                st.text_area(
                    f"TikTok {i}",
                    v["tiktok"],
                    height=150
                )

            st.divider()
