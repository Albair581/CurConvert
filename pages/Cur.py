from bs4 import BeautifulSoup
import requests
import streamlit as st
import math
from datetime import datetime


st.set_page_config(
    page_title="Currency Converter",
    page_icon="\U0001F4B5",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': f"mailto:{st.secrets.personal.email}",
        'Report a bug': f"mailto:{st.secrets.personal.email}",
        'About': "轉換匯率計算機, 運用台灣銀行即時匯率A currency converter that uses the Bank of Taiwan's exchange rate."
    }
)


time_engine = datetime.now()

# mongo pass: mongodb+srv://albert:0bz6QR3zHl6X6WYe@user-info.c3bklyl.mongodb.net/?retryWrites=true&w=majority&appName=user-info

# -----init-----
curDist = {
    "美金American Dollars (USD)": 0, 
    "港幣Hong Kong Dollar (HKD)": 1, 
    "英鎊British Pound (GBP)": 2, 
    "澳幣Australian Dollar (AUD)": 3,
    "加拿大幣Canadian Dollar (CAD)": 4,
    "新加坡幣Singapore Dollar (SGD)": 5,
    "瑞士法郎Swiss Franc (CHF)": 6,
    "日圓Japanese Yen (JPY)": 7,
    "南非幣South African Rand (ZAR)": 8,
    "瑞典幣Swedish Krona (SEK)": 9,
    "紐元New Zealand Dollar (NZD)": 10,
    "泰幣Thai Baht (THB)": 11,
    "菲國比索Philippine Peso (PHP)": 12,
    "印尼幣Indonesian Rupiah (IDR)": 13,
    "歐元Euro (EUR)": 14,
    "韓元Korean Won (KRW)": 15,
    "越南盾Vietnam Dong (VND)": 16,
    "馬來幣Malaysian Ringgit (MYR)": 17,
    "人民幣Chinese Yuan (CNY)": 18,
    "台幣New Taiwan Dollars (NTD)": 19,
}

curList = [
    "美金American Dollars (USD)", 
    "港幣Hong Kong Dollar (HKD)", 
    "英鎊British Pound (GBP)", 
    "澳幣Australian Dollar (AUD)",
    "加拿大幣Canadian Dollar (CAD)",
    "新加坡幣Singapore Dollar (SGD)",
    "瑞士法郎Swiss Franc (CHF)",
    "日圓Japanese Yen (JPY)",
    "南非幣South African Rand (ZAR)",
    "瑞典幣Swedish Krona (SEK)",
    "紐元New Zealand Dollar (NZD)",
    "泰幣Thai Baht (THB)",
    "菲國比索Philippine Peso (PHP)",
    "印尼幣Indonesian Rupiah (IDR)",
    "歐元Euro (EUR)",
    "韓元Korean Won (KRW)",
    "越南盾Vietnam Dong (VND)",
    "馬來幣Malaysian Ringgit (MYR)",
    "人民幣Chinese Yuan (CNY)",
    "台幣New Taiwan Dollars (NTD)",
]

st.title("\U0001F4B5匯率計算機 (來源: 台灣):earth_asia:")
st.header("\U0001F9EECurrency Converter Taiwan Engine")

with st.sidebar:
    st.sidebar.page_link(page="Home.py", label="首頁Home", icon="🏠")
    st.sidebar.page_link(page="pages/Cur.py", label="匯率交換Converter", icon="🧮")
    st.sidebar.page_link(page="pages/Cash.py", label="現金看板Cash Rate Board", icon="💵")
    st.sidebar.page_link(page="pages/Spot.py", label="即期看板Spot Rate Board", icon="💵")
    st.write("---")
    st.header("此計算機運用台灣銀行現時匯率")
    st.subheader("This converter uses the Bank of Taiwan's currencies")
    st.write("---")
    st.header("設定Settings")
    rate = st.radio("選擇匯率Choose a rate",
                    ("即期匯率Spot Rate", "現金匯率Cash Rate"))
    if rate == "即期匯率Spot Rate":
        rateT = "spot"
    else:
        rateT = "cash"
    type = st.radio("選擇計算方式Choose a way to convert",
                    ("一般計算Normal Converting", "平均計算Average Converting"))
    if type == "一般計算Normal Converting":
        typeT = "normal"
    else:
        typeT = "average"
    st.write("---")




def get_currency(url, bank="t"):
    if bank == "t":
        # saves every data
        result = []

        # use requests to get the web info
        response = requests.get(url) 

        # text type appointed to be html original code
        html_doc = response.text 

        # appoint lxml to be BeautifulSoup's finding web engine
        soup = BeautifulSoup(html_doc, "lxml") 

        # find the table with the currency info
        rate_table = soup.find('table').find('tbody')

        rate_table_rows = rate_table.find_all('tr')

        for row in rate_table_rows:
            # analyze every row of data
            columns = row.find_all('td')

            # saves every analyzed data
            data = []
            
            for c in columns:
                if c.attrs['data-table'] == 'Currency':
                    last_div = None
                    divs = c.find_all('div')
                    
                    # get last div tag
                    for last_div in divs:pass
                    
                    # get type of currency
                    data.append(last_div.string.strip())
                elif c.getText().find('Inquiry') != 0 and str(c).find('print_width') > 0 :
                    # save the currency info
                    data.append(c.getText().strip())
            
            # save to analyzed data
            result.append(tuple(data))
        data_time = time_engine.strftime("%b %m, %Y, %a  %I:%M:%S.%f %p")
        return (result, data_time)


amount_from = st.text_input("從From:",
                            key="amountFrom",
                              placeholder="輸入轉換單位數量Enter a currency amount.")
currency_from = st.selectbox("原始貨幣Original Currency:",
                             curList,
                              key="curFrom")

currency_to = st.selectbox("目標貨幣Target Currency:",
                             curList,
                              key="curTo")


convert_btn = st.button("換算Convert!", type="primary")


def convert(p):
    global currency_from, currency_to, curDist, amount_from, ex_result
    try:
        if amount_from != "" and amount_from != " ":
            if not curDist[currency_from] == 19:
                if rateT == "spot":
                    res_from = p[curDist[currency_from]][3]
                else:
                    res_from = p[curDist[currency_from]][1]
            else:
                res_from = "None"
            if not curDist[currency_to] == 19:
                if rateT == "spot":
                    res_to = p[curDist[currency_to]][4]
                else:
                    res_to = p[curDist[currency_to]][2]
            else:
                res_to = "None"

            if typeT == "average":
                if rateT == "spot" and not res_from == "None" and not res_to == "None":
                    if not res_from == "-" and not res_to == "-":
                        res_from = (float(p[curDist[currency_from]][3]) + float(p[curDist[currency_from]][4])) / 2
                        res_to = (float(p[curDist[currency_to]][3]) + float(p[curDist[currency_to]][4])) / 2
                        ex_result = round((float(amount_from) * res_from / float(res_to)), 5)
                    else:
                        ex_result = f"錯誤!請選擇其他匯率或貨幣! ERROR. This currency doesn't have a {rateT} rate for buying and selling. \nThis calculator currently uses the {rateT} rate."
                else:
                    if res_from == "None" or res_to == "None":
                        if currency_from == curList[19]:
                            if not res_to == "None":
                                ex_result = round((float(amount_from) / float(res_to)), 5)
                            else:
                                ex_result = amount_from
                        elif currency_to == curList[19]:
                            ex_result = math.floor(float(amount_from) * float(res_from))
                    else:
                        if not res_from == "-" and not res_to == "-":
                            res_from = (float(p[curDist[currency_from]][1]) + float(p[curDist[currency_from]][2])) / 2
                            res_to = (float(p[curDist[currency_to]][1]) + float(p[curDist[currency_to]][2])) / 2
                            ex_result = round((float(amount_from) * res_from / float(res_to)), 5)
                        else:
                            ex_result = f"錯誤!請選擇其他匯率或貨幣! ERROR. This currency doesn't have a {rateT} rate for buying and selling. \nThis calculator currently uses the {rateT} rate."  
            else:
                if not res_from == "None" and not res_to == "None":
                    if not res_from == "-" and not res_to == "-":
                        ex_result = round((float(amount_from) * float(res_from) / float(res_to)), 5)
                    else:
                        ex_result = f"錯誤!請選擇其他匯率或貨幣! ERROR. This currency doesn't have a {rateT} rate for buying and selling. \nThis calculator currently uses the {rateT} rate."
                else:
                    if currency_from == curList[19]:
                        if not res_to == "None":
                            ex_result = round((float(amount_from) / float(res_to)), 5)
                        else:
                            ex_result = amount_from
                    elif currency_to == curList[19]:
                        ex_result = math.floor(float(amount_from) * float(res_from))
        else:
            ex_result = "錯誤!請輸入數字! ERROR. Please enter numbers."
    except:
        ex_result = "錯誤!請輸入數字! ERROR. Please enter numbers."
    return ex_result


@st.experimental_dialog("計算結果Convertion Result")
def showRes(res):
    st.write(f"<h1>{str(res)}</h1>", unsafe_allow_html=True)


if convert_btn:
    temp = get_currency("https://rate.bot.com.tw/xrt?Lang=en-US", bank="t")
    tempres = convert(temp[0])
    showRes(tempres)
    st.markdown("計算結果Convertion Result")
    st.write(f"<h1>{str(tempres)}</h1>", unsafe_allow_html=True)
    st.caption(f"資料蒐集時間Data collection time: {temp[1]}")


st.write("---")

st.markdown("網站發行家 Website Creator: Albert H.")
