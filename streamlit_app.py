from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Dados básicos do IG:
"""
st.write(""" Perfect""")

# select a number:
n = st.slider("Pick a number", 0,100)

# Read CSV file from GitHub repository
df = pd.read_csv("dados1.csv")

 
 
df.loc[df.index >= 3,'16/01/2023'] = df.loc[df.index >= 3,'16/01/2023'] * n
column = df.loc[df.index >= 1, '16/01/2023'] 

st.dataframe(column)
st.dataframe(df)
st.write(n)
