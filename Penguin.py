import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# 设置页面配置
st.set_page_config(
    page_title="企鹅分类预测",
    page_icon="🐧",
    layout="wide"
)

# 加载图片
def load_logo():
    logo_path = 'public\rigth_logo.png'
    if os.path.exists(logo_path):
        return Image.open(logo_path)
    return None

# 加载企鹅图片
def load_penguin_image(species):
    image_paths = {
        "阿德利企鹅": "public\阿德利企鹅.png",
        "帽带企鹅": "public\帽带企鹅.png",
        "巴布亚企鹅": "public\巴布亚企鹅.png"
    }
    
    if species in image_paths:
        image_path = image_paths[species]
        if os.path.exists(image_path):
            return Image.open(image_path)
    return None

# 加载数据
def load_data():
    data_path = "public\（企鹅识别数据）penguins-chinese.csv"
    try:
        df = pd.read_csv(data_path, encoding='gbk')
        df = df.dropna()
        return df
    except Exception as e:
        st.error(f"加载数据失败: {e}")
        return None

# 训练模型
def train_model(df):
    # 准备特征和标签
    X = df[['喙的长度', '喙的深度', '翅膀的长度', '身体质量']]
    y = df['企鹅的种类']
    
    # 编码标签
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # 训练模型
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y_encoded)
    
    return model, le

# 主应用
def main():
    # 侧边栏
    with st.sidebar:
        st.title("活动选项")
        if load_logo():
            st.image(load_logo(), width=100)
        st.write("---")
        st.write("点击左侧的活动选项，才可以继续预测")
        
        # 活动选项
        activity = st.selectbox(
            "选择活动",
            ["企鹅分类预测", "其他活动1", "其他活动2", "其他活动3"]
        )

    # 主内容区域
    st.title("🐧 预测企鹅分类")
    st.write("你可以通过调整以下参数来预测企鹅的分类，我们将根据机器学习模型为你预测结果！")
    
    # 加载数据和训练模型
    df = load_data()
    if df is None:
        return
    
    model, le = train_model(df)

    # 预测执行模型
    st.subheader("预测执行模型")
    st.write("请选择要使用的预测模型：")
    
    model_option = st.radio(
        "选择模型",
        ["随机森林模型", "支持向量机模型", "决策树模型"]
    )
    
    # 六个输入选项
    st.subheader("输入参数")
    
    # 选项1: 企鹅栖息的岛屿
    island = st.selectbox(
        "企鹅栖息的岛屿",
        df['企鹅栖息的岛屿'].unique()
    )
    
    # 选项2: 性别
    gender = st.selectbox(
        "性别",
        df['性别'].unique()
    )
    
    # 选项3: 喙的长度
    bill_length = st.slider(
        "喙的长度 (mm)",
        min_value=float(df['喙的长度'].min()),
        max_value=float(df['喙的长度'].max()),
        value=float(df['喙的长度'].mean()),
        step=0.1
    )
    
    # 选项4: 喙的深度
    bill_depth = st.slider(
        "喙的深度 (mm)",
        min_value=float(df['喙的深度'].min()),
        max_value=float(df['喙的深度'].max()),
        value=float(df['喙的深度'].mean()),
        step=0.1
    )
    
    # 选项5: 翅膀的长度
    flipper_length = st.slider(
        "翅膀的长度 (mm)",
        min_value=float(df['翅膀的长度'].min()),
        max_value=float(df['翅膀的长度'].max()),
        value=float(df['翅膀的长度'].mean()),
        step=1.0
    )
    
    # 选项6: 身体质量
    body_mass = st.slider(
        "身体质量 (g)",
        min_value=float(df['身体质量'].min()),
        max_value=float(df['身体质量'].max()),
        value=float(df['身体质量'].mean()),
        step=50.0
    )
    
    # 预测按钮
    if st.button("开始预测"):
        # 使用随机森林模型进行预测
        features = np.array([[bill_length, bill_depth, flipper_length, body_mass]])
        prediction_encoded = model.predict(features)[0]
        prediction = le.inverse_transform([prediction_encoded])[0]
        
        # 显示预测结果
        st.subheader("预测结果")
        
        # 显示使用的模型
        st.write(f"使用的模型: {model_option}")
        
        # 映射关系实例
        st.subheader("映射关系实例")
        
        mapping_result = {
            "预测出的企鹅类别（编码）": prediction_encoded,
            "转换为数据预处理的格式": f"[{bill_length}, {bill_depth}, {flipper_length}, {body_mass}]",
            "预测出的企鹅名称": prediction,
        }
        
        for key, value in mapping_result.items():
            st.write(f"{key}: {value}")
        
        # 显示对应企鹅图片
        st.subheader("预测出的企鹅图片")
        penguin_image = load_penguin_image(prediction)
        if penguin_image:
            st.image(penguin_image, caption=prediction, width=200)
        else:
            st.write("未找到对应企鹅图片")

# 运行应用
if __name__ == '__main__':
    main()