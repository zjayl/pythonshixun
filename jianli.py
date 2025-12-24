import streamlit as st

# 设置页面配置
st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")

# 标题
st.title("个人简历生成器")

# 创建两栏布局
left_col, right_col = st.columns(2)

# 左侧：个人信息表单
with left_col:
    st.header("个人信息表单")
    
    # 个人基本信息
    name = st.text_input("姓名")
    gender = st.radio("性别", ["男", "女"])
    age = st.number_input("年龄", min_value=18, max_value=100, value=25)
    phone = st.text_input("电话")
    email = st.text_input("邮箱")
    location = st.text_input("地址")
    
    # 个人简介
    st.subheader("个人简介")
    bio = st.text_area("请输入个人简介", height=100)
    
    # 技能部分
    st.subheader("技能")
    skills = {
        "Python": st.slider("Python", 0, 100, 85),
        "JavaScript": st.slider("JavaScript", 0, 100, 75),
        "HTML/CSS": st.slider("HTML/CSS", 0, 100, 90),
        "React": st.slider("React", 0, 100, 70),
        "Node.js": st.slider("Node.js", 0, 100, 65)
    }
    
    # 工作经验
    st.subheader("工作经验")
    company = st.text_input("公司名称")
    position = st.text_input("职位")
    start_date = st.date_input("开始日期")
    end_date = st.date_input("结束日期")
    experience = st.text_area("工作描述", height=100)

# 右侧：简历实时预览
with right_col:
    st.header("简历实时预览")
    
    # 个人信息预览
    st.subheader(name)
    st.write(f"{gender} | {age}岁")
    st.write(f"电话: {phone}")
    st.write(f"邮箱: {email}")
    st.write(f"地址: {location}")
    
    # 个人简介预览
    st.subheader("个人简介")
    st.write(bio if bio else "请填写个人简介")
    
    # 技能预览
    st.subheader("技能")
    for skill, level in skills.items():
        st.write(f"{skill}: {level}%")
        st.progress(level)
    
    # 工作经验预览
    st.subheader("工作经验")
    st.write(f"{company} - {position}")
    st.write(f"{start_date} 至 {end_date}")
    st.write(experience if experience else "请填写工作描述")

# 保存简历按钮
if st.button("保存简历"):
    st.success("简历已保存!")
    # 这里可以添加保存逻辑，比如生成PDF或导出为其他格式