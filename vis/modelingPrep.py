"""
Created By: Carson Rupp
5-13-2020

Summary:
This script uses the API from financialmodelingprep, it is good for comparing
multiple different stocks on one graph, can also be used just for one stock.
Seems to be geared towards long term analysis because it is incremented by day.

Issues:
If the stock was not publicly traded at the start date, it will not show
on the plot
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Companies to Analyze
companies = ["SHOP","CRM","WORK"]
#DF to add to
dflist = []

#Example API request
requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/aapl?serietype=line")

for company in companies:
    prices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{company}?serietype=line")
    #Convert to json
    prices = prices.json()
    #Select the last X days of prices (start day:stop day)
    prices = prices['historical'][-200:]
    #Create a pandas DF
    pricesdf = pd.DataFrame.from_dict(prices)
    pricesdf = pricesdf.rename({'close': company}, axis = 1)
    dflist.append(pricesdf)

dfs = [df.set_index('date') for df in dflist]
allprices = pd.concat(dfs,axis=1)
allprices = allprices/allprices.iloc[0]
for i, col in enumerate(allprices.columns) :
    allprices[col].plot()
plt.title("Price Comparisons")
plt.xticks(rotation=70)
plt.legend(allprices.columns)
plt.show()
