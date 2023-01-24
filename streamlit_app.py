from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Datos de las páginas de instagram, tiktok, youtube y telegram: DR.Focus:
"""

# Read CSV file from GitHub repository
df = pd.read_csv("dados1.csv")
df2 = df 

st.write("""Datos fecha: 16/01/2023""")
st.dataframe(df['16/01/2023']) 
st.write("""Datos completos:""")
st.dataframe(df)



# select a number:
n = st.slider("Elija aqui cuanto te gustaria crecer eses resultados de cada metrica:", 1,100)
# MULTIPLICATE THE LAST DATE AND ALL DF
 
df2.iloc[:,1:] = df2.iloc[:,1:] * n
column = df2['16/01/2023'] 

st.write("Asi serian sus resultados con un crescimiento de: {}".format(n))
st.dataframe(df2)
st.dataframe(column)
