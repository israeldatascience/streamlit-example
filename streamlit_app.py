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

 
 
df.loc[df.index >= 3,'DECIEMBRE'] = df.loc[df.index >= 3,'DECIEMBRE'] * n
column = df.loc[df.index >= 1, 'DECIEMBRE'] 

st.dataframe(column)
st.dataframe(df)
st.write(n)
