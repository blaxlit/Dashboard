import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('discord_data.csv')

st.set_page_config(page_title="Discord Dashboard", layout="wide")
st.title("🎮 Discord Server Analytics")
st.sidebar.header("Filter Options")
channel_list = df['Channel'].unique()
selected_channel = st.sidebar.selectbox("เลือกห้อง (Channel)", channel_list)