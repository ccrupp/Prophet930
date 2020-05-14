import requests
import pandas as pd
import matplotlib.pyplot as plt

#Companies to Analyze
companies = ["SHOP","CRM","WORK"]

#DF to add to
df = []

#API request
print (requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/aapl?serietype=line"))
