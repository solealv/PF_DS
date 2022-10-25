import streamlit as st
import pandas as pd
from classes.route import MultiApp
from models import quienes_somos, eje_salud, eje_economico, eje_edu_ambiente, eje_politico, vision_global


app = MultiApp()

app.add_app("Quienes somos", quienes_somos.app)
app.add_app("Eje salud", eje_salud.app)
app.add_app("Eje economico", eje_economico.app)
app.add_app("Eje eucacion y ambiente", eje_edu_ambiente.app)
app.add_app("Eje politico", eje_politico.app)
app.add_app("Vision global", vision_global.app)


app.run()
