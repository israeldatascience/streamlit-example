from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Dados básicos do IG:
"""

# Read CSV file from GitHub repository
df = pd.read_csv("dados1.csv")
df2 = df 

st.write("""LAST MEASURE - YOUR RESULTS""")
st.dataframe(df['16/01/2023']) 
st.dataframe(df)

# select a number:
n = st.slider("Choose a multiplier of your growth - DESIRED GROWTH:", 2,100)
# MULTIPLICATE THE LAST DATE AND ALL DF
 
df3.iloc[:,1:] = df3.iloc[:,1:] * n
column = df2['16/01/2023'] 

st.write("""DESIRED GROWTH: """)
st.dataframe(df3)
st.dataframe(column)
