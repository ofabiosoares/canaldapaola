import streamlit as st
import webbrowser
from st_functions import st_button, load_css
from PIL import Image

load_css()

#ajustando o cabecalho
st.write('<style>div.block-container{padding-top:0.2rem;}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col2.image(Image.open('logo.png'))

#st.header('Paola Bitencourt, AAI')
st.markdown("<h1 style='text-align: center; color: black; font-weight: bold;'>Paola Bitencourt, AAI</h1>", unsafe_allow_html=True)

st.info('Pós Graduando Finanças, Investimentos e Banking pela PUC-RS e Assessora de Investimentos na Wide/XP Investimentos')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@paolabitt', 'Canal da Paola ', icon_size)
st_button('aposentei', 'https://aquirende-previdencia.streamlit.app', 'Simule sua Aposentadoria', icon_size)
#st_button('medium', 'https://www.instagram.com/', 'Lifestyle', icon_size)
st_button('twitter', 'https://twitter.com/apaolabitt/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://linkedin.com/in/paola-bitencourt-aai-97aa35177', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://go.hotmart.com/I93272490Y', 'Adquira meu Ebook!', icon_size)
