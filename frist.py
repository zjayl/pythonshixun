import streamlit as st
import pandas as pd
import numpy as np

# 页面配置
st.set_page_config(page_title="南宁美食数据仪表盘", layout="wide", initial_sidebar_state="collapsed")

# --- 1. 基础餐厅数据 ---
restaurants_data = {
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [15, 20, 25, 35, 50],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
}
df_rest = pd.DataFrame(restaurants_data)

# --- 2. 12个月价格走势数据（5家餐厅） ---
months = [f"{i}月" for i in range(1, 13)]
price_trend_data = {
    "月份": months,
    "星艺会尝不忘": np.linspace(14, 16, 12),
    "高峰柠檬鸭": np.linspace(19, 22, 12),
    "复记老友粉": np.linspace(24, 27, 12),
    "好友缘": np.linspace(33, 38, 12),
    "西冷牛排店": np.linspace(48, 55, 12)
}
df_trend = pd.DataFrame(price_trend_data)

# --- 3. 用餐高峰时段数据（模拟） ---
hours = [f"{h}:00" for h in range(10, 22)]
peak_data = {
    "时段": hours,
    "客流量": [50, 80, 120, 150, 200, 180, 160, 220, 250, 200, 150, 100]
}
df_peak = pd.DataFrame(peak_data)

# --- 页面布局 ---
st.title("南宁美食数据仪表盘")

# 第一行：地图 + 评分柱状图
col1, col2 = st.columns(2)
with col1:
    st.subheader("餐厅分布地图")
    st.map(df_rest[["latitude", "longitude"]], zoom=11)

with col2:
    st.subheader("餐厅评分")
    st.bar_chart(df_rest, x="餐厅", y="评分", color="#1f77b4")

# 第二行：不同类型餐厅价格 + 12个月价格走势
col3, col4 = st.columns(2)
with col3:
    st.subheader("不同类型餐厅价格")
    st.line_chart(df_rest, x="类型", y="人均消费(元)", color="#ff7f0e")

with col4:
    st.subheader("5家餐厅12个月价格走势")
    st.line_chart(df_trend, x="月份", y=df_rest["餐厅"].tolist(), color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"])

# 第三行：用餐高峰时段 + 餐厅详情
col5, col6 = st.columns(2)
with col5:
    st.subheader("用餐高峰时段")
    st.area_chart(df_peak, x="时段", y="客流量", color="#2ca02c")

with col6:
    st.subheader("餐厅详情")
    st.dataframe(
        df_rest[["餐厅", "类型", "评分", "人均消费(元)"]],
        hide_index=True,
        column_config={
            "评分": st.column_config.NumberColumn(format="%.1f"),
            "人均消费(元)": st.column_config.NumberColumn(format="¥%d")
        }
    )

# 第四行：今日午餐推荐
st.subheader("今日午餐推荐")
st.image("https://img95.699pic.com/photo/50162/1314.jpg_wh860.jpg", caption="老友粉（复记老友粉招牌菜）", use_column_width=True)
