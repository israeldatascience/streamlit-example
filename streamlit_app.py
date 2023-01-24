from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Dados básicos do IG:
"""
st.write(""" Perfect""")

# Read CSV file from GitHub repository
df = pd.read_csv("data1.csv")

# Display data in a Streamlit dataframe
st.dataframe(df)
