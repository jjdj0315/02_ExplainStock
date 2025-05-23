import streamlit as st
import plotly.graph_objects as go

from utils.search import stock_search
from utils.searchresult import SearchResult
from utils.load_stock import Stock
from utils.create_report import cache_AI_report
#검색창
st.title("주식 정보 분석 대시보드")

search_query = st.text_input("검색창")
hits = stock_search(search_query)['hits']
search_result = [SearchResult(hit) for hit in hits]

selected = st.selectbox("검색결과 리스트", search_result)

#회사 기본정보, AI분석 보고서, 종목토론실
tabs = ["회사 기본 정보", " AI 분석 보고서", "종목토론실"]
tab1, tab2, tab3 = st.tabs(tabs)

with tab1:
    stock = Stock(selected.symbol)
    st.header(str(selected))
    stock_data = stock.금융정보()
    # 주가 시각화
    st.subheader(f"{selected.symbol }주가")
    candlestick = go.Candlestick(
        x=stock_data["history"].index,
        open=stock_data["history"]["Open"],
        high=stock_data["history"]["High"],
        low=stock_data["history"]["Low"],
        close=stock_data["history"]["Close"],
    )
    fig = go.Figure(candlestick)
    st.plotly_chart(fig)
    # 거래량 시각화
    st.subheader(f"{selected.symbol}거래량")
    st.bar_chart(stock_data["history"]["Volume"])

    st.header(f"{selected.symbol }재무제표")
    cols = st.columns(3)
    cols[0].subheader("매출액")
    cols[0].line_chart(stock_data["income_statement"].loc["Total Revenue"])
    cols[1].subheader("순이익")
    cols[1].line_chart(stock_data["income_statement"].loc["Net Income"])
    cols[2].subheader("영업이익")
    cols[2].line_chart(stock_data["income_statement"].loc["Operating Income"])

    cols = st.columns(3)
    cols[0].subheader("자산")
    cols[0].line_chart(stock_data["balance_sheet"].loc["Total Assets"])
    cols[1].subheader("부채")
    cols[1].line_chart(
        stock_data["balance_sheet"].loc["Total Liabilities Net Minority Interest"]
    )
    cols[2].subheader("자본")
    cols[2].line_chart(stock_data["balance_sheet"].loc["Stockholders Equity"])
    cols = st.columns(4)
    cols[0].subheader("영업 현금흐름")
    cols[0].line_chart(stock_data["cash_flow"].loc["Operating Cash Flow"])
    cols[1].subheader("투자 현금흐름")
    cols[1].line_chart(stock_data["cash_flow"].loc["Investing Cash Flow"])
    cols[2].subheader("재무 현금흐름")
    cols[2].line_chart(stock_data["cash_flow"].loc["Financing Cash Flow"])
    cols[3].subheader("순 현금흐름")
    cols[3].line_chart(stock_data["cash_flow"].loc["Free Cash Flow"])    
    
with tab2:
    st.header("AI분석 보고서")
    if st.button("보고서 불러오기"):
        with st.spinner(text = "In progress"):
            data = cache_AI_report(selected.symbol)
