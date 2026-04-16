import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:123456@localhost:5432/iot')

def load_data(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

st.title('Dashboard IoT')

st.header('Média de temperatura por sala')
df1 = load_data('avg_temp_por_dispositivo')
st.plotly_chart(px.bar(df1, x='room_id', y='avg_temp'))

st.header('Leituras por hora')
df2 = load_data('leituras_por_hora')
st.plotly_chart(px.line(df2, x='hora', y='contagem'))

st.header('Temperatura máxima e mínima por dia')
df3 = load_data('temp_max_min_por_dia')
st.plotly_chart(px.line(df3, x='data', y=['temp_max','temp_min']))