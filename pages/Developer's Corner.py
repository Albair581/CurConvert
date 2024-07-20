import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="Developer's Corner",
    page_icon="\U0001F4BB",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:albertoyucheng@gmail.com',
        'Report a bug': "mailto:albertoyucheng@gmail.com",
    }
)

st.title("\U0001F4BB開發者專區Developer's Corner")
st.header("歡迎來到開發者專區!\nWelcome to the developer's corner!")
st.write("在這裡, 你可以知道如何運用我們的網站!      \nHere, you can get how to use our web,\n and take it to your own advantage!")
st.write("###")
st.subheader("如何運用此網站的匯率表? \nHow to use our currency list?")
st.write('---')
st.write("你可以運用網站爬蟲的功能, 爬取以下列表。")
st.write("You can use the web scraping functions in your code to scrape the list below.")

def get_currency():
    # saves every data
    result = []

    # use requests to get the web info
    response = requests.get("https://rate.bot.com.tw/xrt?Lang=en-US") 

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
    return result

list = get_currency()
st.write(list)

st.write("---")
st.header("Thank you for using our information!")
