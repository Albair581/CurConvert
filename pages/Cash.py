import streamlit as st
from Home import get_currency
import math

st.set_page_config(
    page_title="Spot Board",
    page_icon="\U0001F4B5",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': f"mailto:{st.secrets.personal.email}",
        'Report a bug': f"mailto:{st.secrets.personal.email}",
        'About': "轉換匯率計算機, 運用台灣銀行即時匯率A currency converter that uses the Bank of Taiwan's exchange rate."
    }
)

st.title("即期匯率轉化看板 Spot Rate Exchange Board")

with st.sidebar:
    st.sidebar.page_link(page="Home.py", label="首頁Home", icon="🏠")
    st.sidebar.page_link(page="pages/Dev.py", label="開發區Developer's Corner", icon="💻")
    st.sidebar.page_link(page="pages/Cash.py", label="現金看板Cash Rate Board", icon="💵")
    st.sidebar.page_link(page="pages/Spot.py", label="即期看板Spot Rate Board", icon="💵")

curList = ["ntd", "cny", "jpy", "usd", "gbp", "eur", "vnd"]

if "ntd" not in st.session_state:
    st.session_state.ntd = "v"
    st.session_state.ntd = ""
if "cny" not in st.session_state:
    st.session_state.cny = "v"
    st.session_state.cny = ""
if "jpy" not in st.session_state:
    st.session_state.jpy = "v"
    st.session_state.jpy = ""
if "usd" not in st.session_state:
    st.session_state.usd = "v"
    st.session_state.usd = ""
if "gbp" not in st.session_state:
    st.session_state.gbp = "v"
    st.session_state.gbp = ""
if "eur" not in st.session_state:
    st.session_state.eur = "v"
    st.session_state.eur = ""

currency = 0

def ntdElse():
    global currency
    currency = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US")
    st.session_state.cny = str(round((float(st.session_state.ntd) / float(currency[18][2])), 5))
    st.session_state.jpy = str(round((float(st.session_state.ntd) / float(currency[7][2])), 5))
    st.session_state.usd = str(round((float(st.session_state.ntd) / float(currency[0][2])), 5))
    st.session_state.gbp = str(round((float(st.session_state.ntd) / float(currency[2][2])), 5))
    st.session_state.eur = str(round((float(st.session_state.ntd) / float(currency[14][2])), 5))

def cnyElse():
    global currency
    currency = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US")
    st.session_state.ntd = str(math.floor(float(st.session_state.cny) * float(currency[18][1])))
    st.session_state.jpy = str(round(((float(st.session_state.cny) * float(currency[18][1])) / float(currency[7][2])), 5))
    st.session_state.usd = str(round(((float(st.session_state.cny) * float(currency[18][1])) / float(currency[0][2])), 5))
    st.session_state.gbp = str(round(((float(st.session_state.cny) * float(currency[18][1])) / float(currency[2][2])), 5))
    st.session_state.eur = str(round(((float(st.session_state.cny) * float(currency[18][1])) / float(currency[14][2])), 5))

def jpyElse():
    global currency
    currency = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US")
    st.session_state.ntd = str(math.floor(float(st.session_state.jpy) * float(currency[7][1])))
    st.session_state.cny = str(round(((float(st.session_state.jpy) * float(currency[7][1])) / float(currency[18][2])), 5))
    st.session_state.usd = str(round(((float(st.session_state.jpy) * float(currency[7][1])) / float(currency[0][2])), 5))
    st.session_state.gbp = str(round(((float(st.session_state.jpy) * float(currency[7][1])) / float(currency[2][2])), 5))
    st.session_state.eur = str(round(((float(st.session_state.jpy) * float(currency[7][1])) / float(currency[14][2])), 5))

def usdElse():
    global currency
    currency = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US")
    st.session_state.ntd = str(math.floor(float(st.session_state.usd) * float(currency[0][1])))
    st.session_state.cny = str(round(((float(st.session_state.usd) * float(currency[0][1])) / float(currency[18][2])), 5))
    st.session_state.jpy = str(round(((float(st.session_state.usd) * float(currency[0][1])) / float(currency[7][2])), 5))
    st.session_state.gbp = str(round(((float(st.session_state.usd) * float(currency[0][1])) / float(currency[2][2])), 5))
    st.session_state.eur = str(round(((float(st.session_state.usd) * float(currency[0][1])) / float(currency[14][2])), 5))

def gbpElse():
    global currency
    currency = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US")
    st.session_state.ntd = str(math.floor(float(st.session_state.gbp) * float(currency[2][1])))
    st.session_state.cny = str(round(((float(st.session_state.gbp) * float(currency[2][1])) / float(currency[18][2])), 5))
    st.session_state.jpy = str(round(((float(st.session_state.gbp) * float(currency[2][1])) / float(currency[7][2])), 5))
    st.session_state.usd = str(round(((float(st.session_state.gbp) * float(currency[2][1])) / float(currency[0][2])), 5))
    st.session_state.eur = str(round(((float(st.session_state.gbp) * float(currency[2][1])) / float(currency[14][2])), 5))

def eurElse():
    global currency
    currency = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US")
    st.session_state.ntd = str(math.floor(float(st.session_state.eur) * float(currency[14][1])))
    st.session_state.cny = str(round(((float(st.session_state.eur) * float(currency[14][1])) / float(currency[18][2])), 5))
    st.session_state.jpy = str(round(((float(st.session_state.eur) * float(currency[14][1])) / float(currency[7][2])), 5))
    st.session_state.usd = str(round(((float(st.session_state.eur) * float(currency[14][1])) / float(currency[0][2])), 5))
    st.session_state.gbp = str(round(((float(st.session_state.eur) * float(currency[14][1])) / float(currency[2][2])), 5))

def clear():
    st.session_state.ntd = ""
    st.session_state.cny = ""
    st.session_state.jpy = ""
    st.session_state.usd = ""
    st.session_state.gbp = ""
    st.session_state.eur = ""

if st.session_state.ntd:
    ntdElse()
elif st.session_state.cny:
    cnyElse()
elif st.session_state.jpy:
    jpyElse()
elif st.session_state.usd:
    usdElse()
elif st.session_state.gbp:
    gbpElse()
elif st.session_state.eur: 
    eurElse()

reset = st.button("清空Clear")
if reset:
    clear()
ntd = st.text_input("台幣NTD", key="ntd")
cny = st.text_input("人民幣CNY", key="cny")
jpy = st.text_input("日圓JPY", key="jpy")
usd = st.text_input("美金USD", key="usd")
gbp = st.text_input("英鎊GBP", key="gbp")
eur = st.text_input("歐元EUR", key="eur")