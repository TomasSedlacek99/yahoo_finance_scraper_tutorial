import requests
from bs4 import BeautifulSoup
import time

urls = ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOG/", "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"]
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

for url in urls:
    html_page = requests.get(url, headers=headers)

    soup = BeautifulSoup(html_page.content, 'lxml')

    #Header with important info filtered
    header_info = soup.find_all("div", id="quote-header-info")[0]

    #Stock title tag on the website
    stock_title = header_info.find("h1").get_text()

    #Current price extraction
    current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px) W(100%)").find("fin-streamer").get_text()

    #Info table filtering
    quote_summary = soup.find_all("div", id="quote-summary")[0]
    table_left = quote_summary.find_all("table")[0].find_all("tr")
    table_right = quote_summary.find_all("table")[1].find_all("tr")

    print()
    print(stock_title)
    print(current_price)

    #Left side table data extraction
    for index in range(0,8):
        heading = table_left[index].find("span").get_text()
        value = table_left[index].find_all("td")[1].get_text()
        print(heading + ": " + value)

    #Right side table data extraction
    for index in range(0,8):
        heading = table_right[index].find("span").get_text()
        value = table_right[index].find_all("td")[1].get_text()
        print(heading + ": " + value)

    time.sleep(5)