import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components

# URL do backend Flask
api_url = "http://127.0.0.1:5000/mapa"

st.set_page_config(initial_sidebar_state="collapsed")

# Solicita os dados da API
response = requests.get(api_url)
markers = response.json()  # Recebe os dados em formato JSON

# Cria o mapa centrado em uma das localizações, por exemplo, São Paulo
m = folium.Map(location=[-23.5986884,-46.6765147], zoom_start=15)

# Adiciona marcadores com os dados da API
for marker in markers:
    folium.Marker(
        [marker["lat"], marker["lon"]],
        popup=marker["info"],
        tooltip=marker["name"]
    ).add_to(m)

# Renderiza uma seção de cabeçalho personalizada usando HTML e CSS
with open("templates/map.html", "r", encoding="utf-8") as file:
    html_code = file.read()

components.html(html_code, height=120)

# Exibe o mapa no Streamlit
st.write("Mapa Interativo")
st_folium(m, width=700, height=500)