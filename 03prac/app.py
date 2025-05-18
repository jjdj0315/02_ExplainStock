import streamlit as st


st.title("주식 정보 분석 대시보드")

search_query = st.text_input("검색창")
hits =stock_search(search_query)["hits"]
