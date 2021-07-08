import csv
import yfinance as yf
import numpy as np

# stocks = []

# with open("data.csv", mode='r',) as data:
#     data_reader = csv.DictReader(data)

#     for row in data_reader:
#         stock = (row['Symbol'])
#         try:
#             req_stock = yf.Ticker(stock)
#             stocks.append(req_stock.info.get("symbol"))
#         except:
#             print("Couldnt find ticker")

# data = np.array(stocks)

# np.savetxt("Results", data, fmt='%s')


dict = {}

with open("Results.csv", mode='r',) as data:
    data_reader = csv.DictReader(data)

    for row in data_reader:
        stock = (row['Symbol'])
        req_stock = yf.Ticker(stock)
        stock_info = req_stock.info
        stock_symbol = stock_info.get("symbol")

        try:
            stock_price = int(stock_info.get("previousClose"))
            stock_sma = int(stock_info.get("fiftyDayAverage"))
            
            if stock_price > stock_sma:
                stock_industry = stock_info.get("industry")

                dict[stock_symbol] = stock_industry
        except:
            print(f"No info for: {stock_symbol}")

print(dict)
