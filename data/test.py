import pprint
pp = pprint.PrettyPrinter(indent = 4)
print = pp.pprint

import requests
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOG&apikey=0GGIM0L0U42EVGVN'
r = requests.get(url)
print(r.json)