import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date

urls = ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOG/", "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"]
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

today = str(date.today()) + ".csv"
csv_file = open(today, "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day`s Range', '52 Week Range', 'Volume', 'Avg. Volume', 'Market Cap',
                     'Beta (5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est'])

for url in urls:
    stock = []
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
    stock.append(stock_title)
    stock.append(current_price)

    #Left side table data extraction
    for index in range(0,8):
        heading = table_left[index].find("span").get_text()
        value = table_left[index].find_all("td")[1].get_text()
        stock.append(value)
        print(heading + ": " + value)

    #Right side table data extraction
    for index in range(0,8):
        heading = table_right[index].find("span").get_text()
        value = table_right[index].find_all("td")[1].get_text()
        stock.append(value)
        print(heading + ": " + value)

    csv_writer.writerow(stock)
    time.sleep(5)

csv_file.close()

send_mail.send(filename=today)