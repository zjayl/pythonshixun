import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="综合管理系统",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 综合管理系统")

tab1, tab2, tab3 = st.tabs([ "学生数字档案", "美食数据仪表盘","个人简历生成器" ])

with tab1:
    st.title("📊 学生 周健林 -数字档案")
    
    st.header("🔍 基础信息")
    col1, col2 = st.columns([1, 3])
    with col2:
        st.markdown("""
        - **学生ID:** NE0-2025-001
        - **姓名:** 周健林  
        - **注册时间:** 2025-12-01  
        - **指导教师:** 陆紫光 
        - **当前班级:** 2022级 信息管理信息系统 2班  
        """)
    
    st.header("💻 技能矩阵")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("C编程", "95%", "2%")
    with col2:
        st.metric("Python", "87%", "-1%")
    with col3:
        st.metric("Java", "68%", "-3%")
    
    st.subheader("📚 Streamlit课程进度")
    st.progress(78)
    st.text("Streamlit课程进度: 已完成78%")
    
    st.header("📋 任务日志")
    
    tasks_data = {
        "ID": [0, 1, 2],
        "日期": ["2023-10-01", "2023-09-25", "2023-09-12"],
        "任务名称": ["学生管理系统", "课程管理系统", "数据可视化展示"],
        "状态": ["✅ 完成", "🔄 进行中", "❌ 未完成"],
        "难度": ["★★★★★", "★★★★☆", "★★★★☆"]
    }
    
    tasks_df = pd.DataFrame(tasks_data)
    st.table(tasks_df)
    
    st.header("💡 最新代码成果")
    code_example = """
    def attack_search():
        
        while True:
            if detect_vulnerability():
                exploit()
                return "ACCESS GRANTED"
            else:
                stealth_eval()
    """
    st.code(code_example, language="python")
    
    st.markdown("---")
    st.markdown("### 🖥️ 系统信息")
    
    with st.expander("系统日志", expanded=False):
        st.markdown("""
        > **系统消息:** 下一个任务已解锁
        > **任务:** 漏洞管理系统
        > **时间:** 2023-10-15 12:45:38
        """)
    
    st.markdown("""
    <div class='highlight'>
    <span class='status-indicator status-active'></span>
    <strong>系统状态:</strong> 在线监控中 · 已连接
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.title("个人简历生成器")
    
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.header("个人信息表单")
        
        name = st.text_input("姓名")
        gender = st.radio("性别", ["男", "女"])
        age = st.number_input("年龄", min_value=18, max_value=100, value=25)
        phone = st.text_input("电话")
        email = st.text_input("邮箱")
        location = st.text_input("地址")
        
        st.subheader("个人简介")
        bio = st.text_area("请输入个人简介", height=100)
        
        st.subheader("技能")
        skills = {
            "Python": st.slider("Python", 0, 100, 85),
            "JavaScript": st.slider("JavaScript", 0, 100, 75),
            "HTML/CSS": st.slider("HTML/CSS", 0, 100, 90),
            "React": st.slider("React", 0, 100, 70),
            "Node.js": st.slider("Node.js", 0, 100, 65)
        }
        
        st.subheader("工作经验")
        company = st.text_input("公司名称")
        position = st.text_input("职位")
        start_date = st.date_input("开始日期")
        end_date = st.date_input("结束日期")
        experience = st.text_area("工作描述", height=100)
    
    with right_col:
        st.header("简历实时预览")
        
        st.subheader(name)
        st.write(f"{gender} | {age}岁")
        st.write(f"电话: {phone}")
        st.write(f"邮箱: {email}")
        st.write(f"地址: {location}")
        
        st.subheader("个人简介")
        st.write(bio if bio else "请填写个人简介")
        
        st.subheader("技能")
        for skill, level in skills.items():
            st.write(f"{skill}: {level}%")
            st.progress(level)
        
        st.subheader("工作经验")
        st.write(f"{company} - {position}")
        st.write(f"{start_date} 至 {end_date}")
        st.write(experience if experience else "请填写工作描述")
    
    if st.button("保存简历"):
        st.success("简历已保存!")

with tab3:
    st.title("南宁美食数据仪表盘")
    
    def crawl_restaurant_data():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/136.0.0.0 Safari/537.36'}
        url = "https://example.com/nanning-food"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            response.encoding = 'utf-8'
        except:
            return [
                {"餐厅": "星艺会尝不忘", "类型": "中餐", "评分": 4.2, "人均消费(元)": 15},
                {"餐厅": "高峰柠檬鸭", "类型": "中餐", "评分": 4.5, "人均消费(元)": 20},
                {"餐厅": "复记老友粉", "类型": "快餐", "评分": 4.0, "人均消费(元)": 25},
                {"餐厅": "好友缘", "类型": "自助餐", "评分": 4.7, "人均消费(元)": 35},
                {"餐厅": "西冷牛排店", "类型": "西餐", "评分": 4.3, "人均消费(元)": 50}
            ]
        
        soup = BeautifulSoup(response.text, 'lxml')
        restaurant_list = []
        for item in soup.find_all('div', class_='shop-item'):
            shop_data = {}
            shop_data["餐厅"] = item.find('h3', class_='shop-name').get_text().strip() if item.find('h3', class_='shop-name') else "未知"
            shop_data["类型"] = item.find('span', class_='shop-type').get_text().strip() if item.find('span', class_='shop-type') else "未知"
            score = item.find('span', class_='shop-score').get_text().strip() if item.find('span', class_='shop-score') else "0"
            shop_data["评分"] = float(score) if score.replace('.','').isdigit() else 0.0
            price = item.find('span', class_='shop-price').get_text().strip().replace('人均¥','') if item.find('span', class_='shop-price') else "0"
            shop_data["人均消费(元)"] = int(price) if price.isdigit() else 0
            restaurant_list.append(shop_data)
        
        return restaurant_list[:5] if len(restaurant_list)>=5 else restaurant_list + [
            {"餐厅": "星艺会尝不忘", "类型": "中餐", "评分": 4.2, "人均消费(元)": 15},
            {"餐厅": "高峰柠檬鸭", "类型": "中餐", "评分": 4.5, "人均消费(元)": 20},
            {"餐厅": "复记老友粉", "类型": "快餐", "评分": 4.0, "人均消费(元)": 25},
            {"餐厅": "好友缘", "类型": "自助餐", "评分": 4.7, "人均消费(元)": 35},
            {"餐厅": "西冷牛排店", "类型": "西餐", "评分": 4.3, "人均消费(元)": 50}
        ][len(restaurant_list):5]
    
    @st.cache_data
    def preprocess_data():
        raw_data = crawl_restaurant_data()
        df_rest = pd.DataFrame(raw_data)
        df_rest["latitude"] = [22.853838, 22.965046, 22.812200, 22.809105, 22.839699]
        df_rest["longitude"] = [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
        df_rest["评分"] = df_rest["评分"].fillna(df_rest["评分"].median()).clip(0,5)
        df_rest["人均消费(元)"] = df_rest["人均消费(元)"].fillna(df_rest["人均消费(元)"].median()).clip(10,200)
        
        months = [f"{i}月" for i in range(1,13)]
        price_trend = {"月份": months}
        for _, row in df_rest.iterrows():
            price_trend[row["餐厅"]] = np.linspace(row["人均消费(元)"]*0.95, row["人均消费(元)"]*1.05, 12).round(1)
        df_trend = pd.DataFrame(price_trend)
        
        df_peak = pd.DataFrame({
            "时段": [f"{h}:00" for h in range(10,22)],
            "客流量": [50,80,120,150,200,180,160,220,250,200,150,100]
        })
        return df_rest, df_trend, df_peak
    
    df_rest, df_trend, df_peak = preprocess_data()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("餐厅分布地图")
        st.map(df_rest[["latitude", "longitude"]], zoom=11)
    with col2:
        st.subheader("餐厅评分对比")
        st.bar_chart(df_rest, x="餐厅", y="评分", color="#1f77b4", use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("不同类型餐厅人均消费")
        st.line_chart(df_rest, x="类型", y="人均消费(元)", color="#ff7f0e", use_container_width=True)
    with col4:
        st.subheader("5家餐厅12个月价格走势")
        st.line_chart(df_trend, x="月份", y=df_rest["餐厅"].tolist(), use_container_width=True)
    
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("用餐高峰时段客流量")
        st.area_chart(df_peak, x="时段", y="客流量", color="#2ca02c", use_container_width=True)
    with col6:
        st.subheader("餐厅详情表")
        st.dataframe(df_rest[["餐厅", "类型", "评分", "人均消费(元)"]], hide_index=True, use_container_width=True)

st.markdown("---")
col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.write("📧 邮箱：info@example.com")
with col_info2:
    st.write("📞 电话：0771-1234567")
with col_info3:
    st.write("📍 地址：广西南宁市")

st.markdown("""
---
© 2023 综合管理系统 版权所有
""")
