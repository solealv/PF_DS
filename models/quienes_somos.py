import streamlit.components.v1 as components
import streamlit as st
import pandas as pd

def app():

    header_container = st.container()
    dash1_container = st.container()
    dash2_container = st.container()

    with header_container:
        #st.image('./images/calculator.jpg')
        st.title('Ukuphila + Vida')
        st.subheader('Significado mas alla de las fronteras')
        st.write('En zulú, la principal lengua materna de Sudáfrica, ukuphila significa vida. Por esta razón, la elegimos como nombre para nuestra ONG.')
        st.subheader('Buscamos datos y los transformamos en informacion.')
        st.write('Desde la ONG Ukuphila + Vida nos planteamos el objetivo de poner en números el desarrollo humano a nivel global. Para esto, ponemos en marcha un proyecto donde nuestro equipo de científicos, analistas e ingenieros de datos buscarán traducir los datos en información para la sociedad.')

    with dash1_container:
        st.title('Nuestros objetivos')
        st.subheader('Objetivo principal')
        st.write('Identificar la incidencia y manifestación de los principales factores sociales y económicos que tienen correspondencia en la esperanza de vida de una población en un periodo de tiempo y espacio definido.')
        st.subheader('Objetivos generales')
        st.write('* Analizar la evolución histórica de la esperanza de vida en un conjunto de al menos 30 países de diferentes partes del mundo.')
        st.write('* Determinar qué países y/o continentes tienen mejor proyección a futuro con la esperanza de vida.')
        st.write('* Observar y analizar el comportamiento histórico de la esperanza de vida con una antigüedad no menor a 30 años.')
        st.write('* Establecer los principales aspectos económicos, políticos, ambientales, educativos y de salud que tienen relación directa con la esperanza de vida.')
    #with dash2_container:
        

