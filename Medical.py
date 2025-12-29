import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
import os

# 设置页面标题
st.set_page_config(page_title="医疗费用预测Web应用", page_icon="🏥")

# 读取数据函数
def load_data():
    data_path = "./public/（医疗费用预测数据）insurance-chinese.csv"
    # 尝试不同编码读取文件
    df = pd.read_csv(data_path, encoding='gbk')
    # 重命名列名
    df.columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
    return df

# 加载数据
if 'df' not in st.session_state:
    st.session_state.df = load_data()

df = st.session_state.df

# 侧边栏导航
nav = st.sidebar.radio("导航", ["简介", "预测医疗费用"])

if nav == "简介":
    st.title("医疗费用预测Web应用")
    st.write("本应用使用机器学习模型预测医疗费用，为保险公司的保险定价提供参考。")
    st.write("数据来源：医疗费用预测数据集")

elif nav == "预测医疗费用":
    st.title("预测医疗费用")
    st.write("请输入以下信息，系统将预测您的未来医疗费用支出")
    
    # 用户输入界面
    col1 = st.columns(1)[0]
    
    with col1:
        age = st.number_input("年龄", min_value=0, max_value=120, value=30)
        sex = st.radio("性别", ["男性", "女性"])
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
        children = st.number_input("子女数量", min_value=0, max_value=10, value=0)
        smoker = st.radio("是否吸烟", ["是", "否"])
        region = st.selectbox("区域", ["东北部", "西北部", "东南部", "西南部"])
    
    # 预处理用户输入数据
    def preprocess_input(age, sex, bmi, children, smoker, region):
        # 将中文转换为模型可识别的格式
        sex_encoded = 1 if sex == "男性" else 0
        smoker_encoded = 1 if smoker == "是" else 0
        
        # 区域编码
        region_dict = {"东北部": 0, "西北部": 1, "东南部": 2, "西南部": 3}
        region_encoded = region_dict[region]
        
        return np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    
    # 训练模型或加载已训练模型
    def train_model():
        if df is None:
            st.error("数据加载失败，无法训练模型")
            return None
        
        # 数据预处理
        df_copy = df.copy()
        
        # 编码分类变量
        le_sex = LabelEncoder()
        le_smoker = LabelEncoder()
        le_region = LabelEncoder()
        
        df_copy['sex'] = le_sex.fit_transform(df_copy['sex'])
        df_copy['smoker'] = le_smoker.fit_transform(df_copy['smoker'])
        df_copy['region'] = le_region.fit_transform(df_copy['region'])
        
        # 划分特征和目标变量
        X = df_copy.drop('charges', axis=1)
        y = df_copy['charges']
        
        # 划分训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # 特征缩放
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # 训练线性回归模型
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)
        
        return model, scaler
    
    # 预测按钮
    if st.button("预测费用"):
        # 训练模型
        model, scaler = train_model()
        
        if model is not None and scaler is not None:
            # 预处理用户输入
            user_input = preprocess_input(age, sex, bmi, children, smoker, region)
            
            # 特征缩放
            user_input_scaled = scaler.transform(user_input)
            
            # 预测
            prediction = model.predict(user_input_scaled)
            
            # 显示结果
            st.success(f"预测医疗费用: ¥{prediction[0]:.2f}")


