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

# Display data in a Streamlit dataframe
df = df.astype(int) #convert to int
df = df.applymap(lambda x: x*n)
 
 
column = df.loc[df.index >= 1, 'SETEMBRO'] 

st.dataframe(column)
st.write(n)
