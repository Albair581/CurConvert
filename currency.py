
import requests
from bs4 import BeautifulSoup

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
        return result
    
