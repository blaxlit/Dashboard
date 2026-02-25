import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('discord_data.csv')

st.set_page_config(page_title="Discord Dashboard", layout="wide")
st.title("🎮 Discord Server Analytics")
st.sidebar.header("Filter Options")
channel_list = df['Channel'].unique()
selected_channel = st.sidebar.selectbox("เลือกห้อง (Channel)", channel_list)
filtered_df = df[df['Channel'] == selected_channel]
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top Users")
    user_counts = filtered_df.groupby('User')['Value'].sum().reset_index()
    fig_bar = px.bar(user_counts, x='User', y='Value', color='User', title="Activity by User")
    st.plotly_chart(fig_bar, use_container_width=True)