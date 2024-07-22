import streamlit as st
import time


st.set_page_config(page_title="Home", 
                   page_icon="\U0001F3E0",
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items={
                        'Get Help': f"mailto:{st.secrets.personal.email}",
                        'Report a bug': f"mailto:{st.secrets.personal.email}",
                        'About': "轉換匯率計算機, 運用台灣銀行即時匯率A currency converter that uses the Bank of Taiwan's exchange rate."
                    }
    )

div1, div2 = st.columns(2)

with div1:
    load_img = st.image("assets/loading.png")

with div2:
    ch = st.header("網站發行家")
    che = st.header("Website Creator")
    c = st.subheader("Albert H.")

load = st.progress(0, text="Loading...")

progresses = ["加載資料中Loading Data... : ", 
              "加載版面中Loading Widgets... : ", 
              "加載檔案中Loading Files... : ",
              "加載程式中Loading Code... : ",
              "加載頁面中Loading Pages... : ",
              "準備中Preparing... : ",
              "馬上就好囉Almost... : "]

for percent in range(100):
    time.sleep(0.002)
    load_text = progresses[percent // 15] + str(percent) + "%"
    load.progress(percent + 1, text=load_text)

load.progress(100, text="完成了!您的準備網頁中 Done! Preparing your website...")

time.sleep(0.1)
load.empty()

load_img.empty()
c.empty()
ch.empty()
che.empty()

st.title("您好, 歡迎使用此匯率計算機!")
st.title("Hello! Thank you for using our currency widget.")

st.header("此網站顧客用功能")
st.header("Our website services")
st.write("---")

st.page_link(page="pages/Cur.py", label="匯率交換Converter", icon="🧮")
st.page_link(page="pages/Cash.py", label="現金看板Cash Rate Board", icon="💵")
st.page_link(page="pages/Spot.py", label="即期看板Spot Rate Board", icon="💵")

st.write("---")

st.markdown("網站發行家 Website Creator: Albert H.")
