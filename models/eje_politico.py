import streamlit.components.v1 as components
import streamlit as st
import pandas as pd

def app():

    header_container = st.container()
    dash1_container = st.container()

    with header_container:
        #st.image('./images/calculator.jpg')
        st.title('Ukuphila + Vida')

    with dash1_container:
        st.subheader('Subtitulo 1')
        st.write('Desarrollo 1 (aca iria una de las paginas del dash, acompañado por textos breves por encima y por debajo)')
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiYTU5MWUzNDYtMmRmNS00ZTE1LTljZGQtMDBhMWM3NzcwMmM4IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9', height=450)
        st.write('Desarrollo 2 (aca iria una de las paginas del dash, acompañado por textos breves por encima y por debajo)')
        
    