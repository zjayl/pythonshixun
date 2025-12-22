import streamlit as st   # 导入Streamlit并用st代表它

# 第一个普通文本展示元素，无工具提示
st.text("这是一个普通文本展示元素。")
# 第二个普通文本展示元素，有工具提示
st.text('这也是一个普通文本展示元素，带有工具提示',help='这是工具提示')
# 第三个普通文本展示元素，展示一些转义字符
st.text('''读者们，\n你们好\t！欢迎学习Streamlit''')