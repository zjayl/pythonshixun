import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import re
from datetime import datetime

# 辅助函数：生成评分星星显示
def get_rating_stars(rating):
    """根据评分值生成星星显示"""
    # 处理NaN值
    if pd.isna(rating):
        return "☆☆☆☆☆"
    
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    
    stars = "⭐" * full_stars
    if half_star:
        stars += "⭐"  # 使用全星星代替半星星，因为Streamlit不直接支持半星星
    stars += "☆" * empty_stars
    
    return stars

# 设置页面配置
st.set_page_config(
    page_title="销售仪表板",
    page_icon="📊",
    layout="wide"
)

# 读取Excel数据文件
data_path = ".\public\（商场销售数据）supermarket_sales.xlsx"
try:
    # 正确读取Excel文件，数据从第2行开始
    df = pd.read_excel(data_path, header=1)
    
    # 处理时间列，从字符串转换为datetime并提取小时
    if '时间' in df.columns:
        df['时间'] = pd.to_datetime(df['时间'], format='%H:%M:%S')
        df['小时'] = df['时间'].dt.hour
    
    # 设置销售额列（实际是总价列）
    if '总价' in df.columns:
        df['销售额'] = df['总价']
    
    # 确保所有必要的列都存在
    required_columns = ['城市', '性别', '顾客类型', '产品类型', '评分', '销售额', '小时']
    for col in required_columns:
        if col not in df.columns:
            st.error(f"数据缺少必要的列: {col}")
            st.stop()
    
    st.success("数据加载成功！")
except Exception as e:
    st.error(f"数据加载失败: {e}")
    st.stop()

# 页面标题
st.title("📊 销售仪表板")

# 创建侧边栏筛选器
with st.sidebar:
    st.header("请筛选数据:")
    
    # 城市筛选
    if '城市' in df.columns:
        city_filter = st.multiselect(
            "选择城市:",
            options=df['城市'].unique(),
            default=df['城市'].unique()
        )
    
    # 性别筛选
    if '性别' in df.columns:
        gender_filter = st.multiselect(
            "选择性别:",
            options=df['性别'].unique(),
            default=df['性别'].unique()
        )
    
    # 顾客类型筛选
    if '顾客类型' in df.columns:
        customer_type_filter = st.multiselect(
            "选择顾客类型:",
            options=df['顾客类型'].unique(),
            default=df['顾客类型'].unique()
        )

# 应用筛选器
df_filtered = df.copy()

if '城市' in df.columns:
    df_filtered = df_filtered[df_filtered['城市'].isin(city_filter)]

if '性别' in df.columns:
    df_filtered = df_filtered[df_filtered['性别'].isin(gender_filter)]

if '顾客类型' in df.columns:
    df_filtered = df_filtered[df_filtered['顾客类型'].isin(customer_type_filter)]

# 主内容区域
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("总销售额:")
    total_sales = df_filtered['销售额'].sum()
    st.write(f"RMB ¥{total_sales:,.0f}")

with col2:
    st.subheader("顾客评分的平均值:")
    avg_rating = df_filtered['评分'].mean()
    stars = get_rating_stars(avg_rating)
    st.write(f"{avg_rating:.1f} {stars}")

with col3:
    st.subheader("每单的平均销售额:")
    avg_sales_per_order = df_filtered['销售额'].mean()
    st.write(f"RMB ¥{avg_sales_per_order:.2f}")

st.divider()

# 图表区域
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("按小时划分的销售额")
    # 创建按小时划分的销售额图表
    hourly_sales = df_filtered.groupby('小时')['销售额'].sum().reset_index()
    
    if not hourly_sales.empty:
        chart1 = alt.Chart(hourly_sales).mark_bar(color='#1f77b4').encode(
            x=alt.X('小时:O', title='小时'),
            y=alt.Y('销售额:Q', title='销售额 (元)'),
            tooltip=['小时', '销售额']
        ).properties(
            width=500,
            height=300
        )
        st.altair_chart(chart1, width='stretch')

with chart_col2:
    st.subheader("按产品类型划分的销售额")
    # 创建按产品类型划分的销售额图表
    product_sales = df_filtered.groupby('产品类型')['销售额'].sum().reset_index()
    product_sales = product_sales.sort_values('销售额', ascending=False)
    
    if not product_sales.empty:
        chart2 = alt.Chart(product_sales).mark_bar(color='#1f77b4').encode(
            x=alt.X('销售额:Q', title='销售额 (元)'),
            y=alt.Y('产品类型:N', title='产品类型', sort='-x'),
            tooltip=['产品类型', '销售额']
        ).properties(
            width=500,
            height=300
        )

        st.altair_chart(chart2, width='stretch')
