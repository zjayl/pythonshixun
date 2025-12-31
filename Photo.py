import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="照片切换器",
    page_icon="📷",
    layout="wide"
)

# 示例图片数据 - 使用在线图片URL和对应的图注
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

# 初始化会话状态来跟踪当前图片索引
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 获取当前图片和图注
current_photo = photos_data[st.session_state.current_index]

# 主要内容区域
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 显示图片
    st.image(current_photo["url"], width=600)
    
    # 显示图注
    st.caption(current_photo["caption"])
    
    # 显示图片计数器
    st.text(f"{st.session_state.current_index + 1} / {len(photos_data)}")
    
    # 切换按钮
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("上一张"):
            st.session_state.current_index = (st.session_state.current_index - 1) % len(photos_data)
            st.rerun()
    
    with btn_col2:
        if st.button("下一张"):
            st.session_state.current_index = (st.session_state.current_index + 1) % len(photos_data)
            st.rerun()