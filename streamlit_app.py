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
number = st.slider("Pick a number", 0,100)

# Read CSV file from GitHub repository
df = pd.read_csv("dados1.csv")

# Display data in a Streamlit dataframe
 
column = df.loc[df.index >= 3, 'SETEMBRO']
st.dataframe(column*number)
