import streamlit.components.v1 as components
import streamlit as st
import pandas as pd

def app():

    header_container = st.container()
    dash1_container = st.container()
    dash2_container = st.container()

    with header_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Ukuphila + Vida')
        espacio.write(' ')
        imagen.image('./images/logo2.png', width= 180)
        
    with dash1_container:
        st.subheader('Subtitulo 1')
        st.write('Desarrollo 1 (aca iria una de las paginas del dash, acompañado por textos breves por encima y por debajo)')
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNWM0NzM2MDgtMmZkOS00MDYwLTgzNTctNmJiZmFmNGYxOTE5IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9', height=450)
        st.write('Desarrollo 2 (aca iria una de las paginas del dash, acompañado por textos breves por encima y por debajo)')
        
    with dash2_container:
        st.subheader('Subtitulo 2')
        st.write('Desarrollo 3 (aca iria otra pagina del dash, acompañado por textos breves por encima y por debajo)')
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNWM0NzM2MDgtMmZkOS00MDYwLTgzNTctNmJiZmFmNGYxOTE5IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection817da2788864c5a49e89', height=450)
        st.write('Desarrollo 4 (aca iria otra pagina del dash, acompañado por textos breves por encima y por debajo)')