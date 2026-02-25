import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('discord_data.csv')

st.set_page_config(page_title="Discord Dashboard", layout="wide")
st.title("🎮 Discord Server Analytics")
st.markdown("**Welcome to the Server Analytics Dashboard**")
st.sidebar.header("Filter Options")
channel_list = df['Channel'].unique()
selected_channel = st.sidebar.selectbox("เลือกห้อง (Channel)", channel_list)
st.sidebar.divider()
filtered_df = df[df['Channel'] == selected_channel]
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top Users")
    user_counts = filtered_df.groupby('User')['Value'].sum().reset_index()
    fig_bar = px.bar(user_counts, x='User', y='Value', color='User', title="Activity by User")
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader("📊 Text vs Voice")
    type_counts = filtered_df.groupby('Activity_Type').size().reset_index(name='Count')
    fig_pie = px.pie(type_counts, names='Activity_Type', values='Count', title="Activity Type Ratio", hole=0.3)
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()
st.subheader("📈 Daily Activity Trend")
daily_activity = filtered_df.groupby('Date')['Value'].sum().reset_index()
fig_line = px.line(daily_activity, x='Date', y='Value', markers=True, title="Activity Over Time")
st.plotly_chart(fig_line, use_container_width=True)