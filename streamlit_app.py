import streamlit as st
import webbrowser
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('logo.png'))

#st.header('Paola Bitencourt, AAI')
st.markdown("<h1 style='text-align: center; color: black; font-weight: bold;'>Paola Bitencourt, AAI</h1>", unsafe_allow_html=True)

st.info('Pós Graduando Finanças, Investimentos e Banking pela PUC-RS e Assessora de Investimentos na Wide/XP Investimentos')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@paolabitt', 'Canal da Paola ', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/apaolabitt/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://linkedin.com/in/paola-bitencourt-aai-97aa35177', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://linkedin.com/in/paola-bitencourt-aai-97aa35177', 'Fale comigo!', icon_size)
