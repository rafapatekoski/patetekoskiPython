import streamlit as st
import pandas as pd
from pathlib import Path
st.write("Funcionando...")

df = pd.read_csv('datasets/listapiloto2024.csv',sep=';', dtype={'RA': str,'SERIE':str})
df['SERIE'] = df['SERIE'].astype(str)
df['SALA'] = df['SALA'].astype(str)
df['SALA'] = df['SERIE'] + df['SALA']
df['ENTRADA'] = pd.to_datetime(df['ENTRADA'], format='%d/%m/%Y')
df['SAIDA'] = pd.to_datetime(df['SAIDA'], format='%d/%m/%Y')
df['NASCIMENTO'] = pd.to_datetime(df['NASCIMENTO'], format='%d/%m/%Y')

st.dataframe(df)