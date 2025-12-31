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

with st.sidebar:
    st.title("🏫 综合管理系统")
    
    nav = st.radio(
        "导航菜单",
        ["首页", "个人简历生成器", "照片切换器", "美食数据仪表盘", "学生数字档案"]
    )

if nav == "首页":
    st.title("广西职业师范学院")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("./public/2021031764.jpg", use_column_width=True)
    
    with col2:
        st.subheader("学校简介")
        st.write("""
        广西职业师范学院（原广西经济管理干部学院）坐落于广西南宁市风景秀丽的邕江之滨、相思湖畔，
        是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培养适应经济社会发展需要的高素质应用型、技术技能型人才职业教育师资。
        """)
        
        st.subheader("学校历史")
        st.write("""
        学校前身为广西经济管理干部学院，创建于1951年的广西省行政干部训练班，
        是广西经济管理人才的摇篮和基地，为广西经济建设和发展做出了不可磨灭的突出贡献。
        """)
    
    st.subheader("学院概况")
    tab1, tab2, tab3 = st.tabs(["师资力量", "学科专业", "教学成果"])
    
    with tab1:
        st.write("我校拥有一支高素质教师队伍，其中教授、副教授等高级职称教师占比超过40%")
        teachers_data = {
            "职称": ["教授", "副教授", "讲师", "助教"],
            "人数": [52, 127, 245, 68]
        }
        df_teachers = pd.DataFrame(teachers_data)
        st.bar_chart(df_teachers.set_index("职称"))
    
    with tab2:
        st.write("学校设有12个二级学院，涵盖经济学、管理学、工学、理学、教育学等八大学科")
        with st.expander("查看所有专业"):
            st.write("- 经济与管理学院：经济学、金融学、会计学、市场营销")
            st.write("- 信息工程学院：计算机科学与技术、软件工程、物联网工程")
            st.write("- 智能制造学院：机械设计制造及其自动化、电气工程及其自动化")
            st.write("- 教育学院：教育学、心理学、学前教育")
    
    with tab3:
        st.write("近年来，学校获得国家级教学成果奖2项，自治区级教学成果奖15项")
        achievements = {
            "年份": [2018, 2019, 2020, 2021, 2022, 2023],
            "成果数量": [2, 3, 2, 3, 2, 3]
        }
        df_achievements = pd.DataFrame(achievements)
        st.line_chart(df_achievements.set_index("年份"))

elif nav == "个人简历生成器":
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

elif nav == "照片切换器":
    st.title("照片切换器")
    
    photos_data = [
        {
            "url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
            "caption": "可爱的橘猫，阳光照射下显得格外温暖"
        },
        {
            "url": "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
            "caption": "黑白猫咪，专注的眼神"
        },
        {
            "url": "https://images.unsplash.com/photo-1511882150382-421056c89033?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80",
            "caption": "小奶猫，好奇心旺盛的样子"
        },
        {
            "url": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
            "caption": "蓝眼睛猫咪，安静地注视着远方"
        }
    ]
    
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    
    current_photo = photos_data[st.session_state.current_index]
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(current_photo["url"], width=600)
        st.caption(current_photo["caption"])
        st.text(f"{st.session_state.current_index + 1} / {len(photos_data)}")
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("上一张"):
                st.session_state.current_index = (st.session_state.current_index - 1) % len(photos_data)
                st.rerun()
        
        with btn_col2:
            if st.button("下一张"):
                st.session_state.current_index = (st.session_state.current_index + 1) % len(photos_data)
                st.rerun()

elif nav == "美食数据仪表盘":
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

elif nav == "学生数字档案":
    st.title("📊 学生 周健林 -数字档案")
    
    st.header("🔍 基础信息")
    col1, col2 = st.columns([1, 3])
    with col2:
        st.markdown("""
        - **学生ID:** NE0-2023-001
        - **姓名:** 周健林  
        - **注册时间:** 2023-09-01  
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

