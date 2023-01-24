from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Dados básicos do IG:
"""
# Read CSV file from GitHub repository
url = "https://github.com/israeldatascience/streamlit-example/blob/master/dados1.csv"
df = pd.read_csv(url)

# Display data in a Streamlit dataframe
st.dataframe(df)
