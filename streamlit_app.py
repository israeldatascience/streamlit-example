from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Dados básicos do IG:
"""
 
    
# Read in the data from the Google Sheets CSV file
data = pd.read_csv("https://docs.google.com/spreadsheets/d/1oq0SyMfRkEGyIP8SpMZWfjKzpn7B_69k59o6l2PqJpE/edit?usp=sharing")

# Create a Streamlit app
st.title("Google Sheets Data")

# Display the data in a table
st.dataframe(data)
