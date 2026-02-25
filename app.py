import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('discord_data.csv')

st.set_page_config(page_title="Discord Dashboard", layout="wide")
st.title("🎮 Discord Server Analytics")