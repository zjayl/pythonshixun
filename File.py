import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 设置页面配置 - 科幻风格
def set_page_config():
    st.set_page_config(
        page_title="学生数字档案",
        page_icon=":satellite:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

# 创建学生数据仪表盘
def main():
    set_page_config()
    
    # 标题
    st.title("📊 学生 周健林 -数字档案")
    
    # 基础信息部分
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
    
    # 技能矩阵部分
    st.header("💻 技能矩阵")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("C编程", "95%", "2%")
    with col2:
        st.metric("Python", "87%", "-1%")
    with col3:
        st.metric("Java", "68%", "-3%")
    
    # 课程进度
    st.subheader("📚 Streamlit课程进度")
    st.progress(78)
    st.text("Streamlit课程进度: 已完成78%")
    
    # 任务日志表格
    st.header("📋 任务日志")
    
    # 创建任务数据
    tasks_data = {
        "ID": [0, 1, 2],
        "日期": ["2023-10-01", "2023-09-25", "2023-09-12"],
        "任务名称": ["学生管理系统", "课程管理系统", "数据可视化展示"],
        "状态": ["✅ 完成", "🔄 进行中", "❌ 未完成"],
        "难度": ["★★★★★", "★★★★☆", "★★★★☆"]
    }
    
    tasks_df = pd.DataFrame(tasks_data)
    st.table(tasks_df)
    
    # 最新代码成果
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
    
    # 系统消息和状态
    st.markdown("---")
    st.markdown("### 🖥️ 系统信息")
    
    with st.expander("系统日志", expanded=False):
        st.markdown("""
        > **系统消息:** 下一个任务已解锁
        > **任务:** 漏洞管理系统
        > **时间:** 2023-10-15 12:45:38
        """)
    
    # 系统状态指示器
    st.markdown("""
    <div class='highlight'>
    <span class='status-indicator status-active'></span>
    <strong>系统状态:</strong> 在线监控中 · 已连接
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
