import os

from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.load_stock import Stock
import streamlit as st
from load_stock import Stock
load_dotenv()

llm = OpenAI(llm = 'gpt-4o', temperature=0, api_key=os.environ["OPENAI_API_KEY"])

def AI_report(ticker):
    prompt = ChatPromptTemplate(
        [
            (
                "system",
                """
                    I want you to act as a Financial Analyst.
                    Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely! First statement contains following content- “Can you tell us what future stock market looks like based upon current conditions ?”.
                    돈의 단위는 '달러'이고 부동소수점을 사용하지말고 3자리 숫자로 표현해줘""",
            ),
            (
                "user",
                '''
                We provide the information necessary for analysis.
                Given markdown reports with triple quotes. 
                As a Financial Analyst, Take a closer look at the numbers in the report and evaluate the company's growth trends and financial stability to help users discuss freely.
                Provide your opinion to people so they can have an open discussion.
                Please provide the report in Korean.
                """
                {markdown}
                """
                ''',
            ),
        ]
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"markdown" : Stock(ticker).report_support()})


@st.cache_data
def cache_AI_report(ticker):
    return AI_report(ticker)