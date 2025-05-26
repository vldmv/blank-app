import streamlit as st

age = st.slider("김정운", min_value=10, max_value=80, value=30, step=5)
st.write("선택한 나이:", age)
