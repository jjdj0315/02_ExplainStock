import streamlit as st
from utils.search import stock_search
from utils.SearchResult import SearchResult
from utils.load_stock import Stock

# Set the page title
st.title("주식 정보 분석 대시보드")

# Create a text input for search
search_query = st.text_input("검색창")
hits = stock_search(search_query)["hits"]
search_results = [SearchResult(hit) for hit in hits]

selected = st.selectbox("검색결과 리스트", search_results)

tabs = ["회사 기본 정보", "AI 분석 보고서", "종목토론실"]
tab1, tab2, tab3 = st.tabs(tabs)

with tab1:
    stock = Stock(selected.symbol)
    st.header(str(selected))
