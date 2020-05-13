import pprint
pp = pprint.PrettyPrinter(indent = 4)
print = pp.pprint

import requests, collections
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=0GGIM0L0U42EVGVN'

#data = None


class url_builder():
  header = 'https://www.alphavantage.co/query?'
  apikey = '0GGIM0L0U42EVGVN'
  
  def build(function, symbol, outputsize, interval = None):
    url = url_builder.header
    url += 'function=' + function
    url += '&symbol=' + symbol
    
    if interval:
      url += '&interval=' + interval
    
    url += '&outputsize=' + outputsize
    url += '&apikey=' + url_builder.apikey
    
    return url
  
  
class Stock():
  def __repr__(self):
    return self.__str__()
  
  def __str__(self):
    #return pp.pformat(self.__dict__)
    #return str(self.__dict__)
    dict = collections.OrderedDict()
    dict['ticker'] = self._ticker
    dict['type'] = self._type
    dict['interval'] = self._interval
    dict['length'] = self._length
    dict['interval_data']= "DATA LIST"
    
    return pp.pformat(dict)
    
    
  def __init__(self):
    self._ticker = None
    self._type = None
    self._interval = None
    self._interval_data = []
    self._length = 0
  
  def _importData(url):
    _data = None
    try:
      _data = requests.get(url).json()
      print('Data imported successfully')
    except:
      print('Unable to import data')
    return _data
  
  
  def INTRADAY(symbol, interval, outputsize = 'compact'):
    stock = Stock()
  
    #url = url_builder.INTRADAY(symbol, interval, outputsize)
  
    url = url_builder.build(
        'TIME_SERIES_INTRADAY',
        symbol,
        outputsize,
        interval
    )
  
    data = Stock._importData(url)
    if data == None:
      return stock
      
    stock._ticker = data['Meta Data']['2. Symbol']
    stock._type = 'INTRADAY'
    stock._interval = data['Meta Data']['4. Interval']
    _intervals_key = 'Time Series (' + stock._interval + ')'
    
    for key in list(data[_intervals_key].keys()):
      interval_data = data[_intervals_key][key]
      stock._interval_data = [Stock_Interval(key, interval_data)] + stock._interval_data
      
    stock._length = len(stock._interval_data)
    
    return stock

  def _no_interval(url, type, intervals_key):
    stock = Stock()
         
    data = Stock._importData(url)
    if data == None:
      return stock
    
    #print(data)
    
    stock._ticker = data['Meta Data']['2. Symbol']
    
    stock._type = type
    
    
    for key in list(data[intervals_key].keys()):
      interval_data = data[intervals_key][key]
      stock._interval_data = [Stock_Interval(key, interval_data)] + stock._interval_data
    
    stock._length = len(stock._interval_data)
    
    return stock

  def DAILY(symbol, outputsize = 'compact'):
    url = url_builder.build('TIME_SERIES_DAILY', symbol, outputsize)
    return Stock._no_interval(url, 'DAILY', 'Time Series (Daily)')
    
  def DAILY_ADJUSTED(symbol, outputsize = 'compact'):
    url = url_builder.build('TIME_SERIES_DAILY_ADJUSTED', symbol, outputsize)
    return Stock._no_interval(url, 'DAILY_ADJUSTED', 'Time Series (Daily)')
  
  def WEEKLY(symbol, outputsize = 'compact'):
    url = url_builder.build('TIME_SERIES_WEEKLY', symbol, outputsize)
    return Stock._no_interval(url, 'WEEKLY', 'Weekly Time Series')
  
  def WEEKLY_ADJUSTED(symbol, outputsize = 'compact'):
    url = url_builder.build('TIME_SERIES_WEEKLY_ADJUSTED', symbol, outputsize)
    return Stock._no_interval(url, 'WEEKLY ADJUSTED', 'Weekly Adjusted Time Series')
  
  def MONTHLY(symbol, outputsize = 'compact'):
    url = url_builder.build('TIME_SERIES_MONTHLY', symbol, outputsize)
    return Stock._no_interval(url, 'MONTHLY', 'Monthly Time Series')
  
  def MONTHLY_ADJUSTED(symbol, outputsize = 'compact'):
    url = url_builder.build('TIME_SERIES_MONTHLY_ADJUSTED', symbol, outputsize)
    return Stock._no_interval(url, 'MONTHLY ADJUSTED', 'Monthly Adjusted Time Series')
  
  def _dict(self):
    interval_list = []
    for interval in self.intervals:
      interval_list += [interval.dict()]
    return interval_list
    
  def get_ticker(self):
    return self._ticker
  ticker = property(get_ticker)
  
  def get_type(self):
    return self._type
  type = property(get_type)
  
  def get_interval(self):
    return self._interval
  interval = property(get_interval)
  
  def interval(self, index):
    return self._interval_data[index]
  
  def get_length(self):
    return self._length
  length = property(get_length)
  
  def get_interval_data(self):
    return self._interval_data
  interval_data = property(get_interval_data)
  
  def get_keys(self):
    key_list = []
    for interval in self._interval_data:
      key_list += [interval.key]
    return key_list
  keys = property(get_keys)
  
  def key(self, index):
    return self._interval_data[index].key
  
  def get_opens(self):
    open_list = []
    for interval in self._interval_data:
      open_list += [interval.open]
    return open_list
  opens = property(get_opens)
  
  def open(self, index):
    return self._interval_data[index].open

  def get_highs(self):
    high_list = []
    for interval in self._interval_data:
      high_list += [interval.high]
    return high_list
  highs = property(get_highs)
  
  def get_highs2(self):
    high_list = []
    for high in self.get_highs():
      high_list += [high, high]
    return high_list
  highs2 = property(get_highs2)
  
  def high(self, index):
    return self._interval_data[index].high
  
  def get_lows(self):
    low_list = []
    for interval in self._interval_data:
      low_list += [interval.low]
    return low_list
  lows = property(get_lows)
  
  def get_lows2(self):
    low_list = []
    for low in self.get_lows():
      low_list += [low, low]
    return low_list
  lows2 = property(get_lows2)
  
  def low(self, index):
    return self._interval_data[index].low
  
  def get_closes(self):
    close_list = []
    for interval in self._interval_data:
      close_list += [interval.close]
    return close_list
  closes = property(get_closes)
  
  def close(self, index):
    return self._interval_data[index].close
  
  def get_closes_adj(self):
    close_list = []
    for interval in self._interval_data:
      close_list += [interval.close_adj]
    return close_list
  closes_adj = property(get_closes_adj)
  
  def close_adj(self, index):
    return self._interval_data[index].close_adj
  
  def get_volumes(self):
    volume_list = []
    for interval in self._interval_data:
      volume_list += [interval.volume]
    return volume_list
  volumes = property(get_volumes)
  
  def volume(self, index):
    return self._interval_data[index].volume
  
  def get_dividends(self):
    dividend_list = []
    for interval in self._interval_data:
      dividend_list += [interval.dividend]
    return dividend_list
  dividends = property(get_dividends)
  
  def dividend(self, index):
    return self._interval_data[index].dividend
  
  def get_split_coefs(self):
    split_coef_list = []
    for interval in self._interval_data:
      split_coef_list += [interval.split_coef]
    return split_coef_list
  split_coefs = property(get_split_coefs)
  
  def split_coef(self, index):
    return self.interval_data[index].split_coef
  
  def get_opens_closes(self):
    oc_list = []
    for interval in self._interval_data:
      oc_list += [interval.open, interval.close]
    return oc_list
  opens_closes = property(get_opens_closes)
  
  def get_index_single(self):
    index_list = []
    for i in range(self._length):
      index_list += [i]
    return index_list
  index_single = property(get_index_single)
  
  def get_index_double(self):
    index_list = []
    for i in range(self._length):
      index_list += [i, i+1]
    return index_list
  index_double = property(get_index_double)

class Stock_Interval():
  
  def dict(self):
    dict = collections.OrderedDict()
    dict['key'] = self._key,
    dict['open'] = self._open,
    dict['high'] = self._high,
    dict['low'] = self._low,
    dict['close'] = self._close,
    dict['close_adj'] = self._close_adj
    dict['volume'] = self._volume
    dict['dividend'] = self._dividend
    dict['split_coef'] = self._split_coef
    return dict
  
  
  def __init__(self, key, data):
    self._key = key
    self._open = data['1. open']
    self._high = data['2. high']
    self._low = data['3. low']
    self._close = data['4. close']
    
    try:
      self._volume = data['5. volume']
      self._close_adj = None
    except:
      self._close_adj = data['5. adjusted close']
      self._volume = data['6. volume']
      self._dividend = data['7. dividend amount']
    
    try:
      self._split_coef = data['8. split coefficient']
    except:
      self._split_coef = None
    
  def get_key(self):
    return self._key
  key = property(get_key)
  
  def get_open(self):
    return float(self._open)
  open = property(get_open)
  
  def get_high(self):
    return float(self._high)
  high = property(get_high)  
    
  def get_low(self):
    return float(self._low)
  low = property(get_low)
  
  def get_close(self):
    return float(self._close)
  close = property(get_close)  
    
  def get_close_adj(self):
    return float(self._close_adj)
  close_adj = property(get_close_adj)
    
  def get_volume(self):
    return int(self._volume)
  volume = property(get_volume)
  
  def get_dividend(self):
    return float(self._dividend)
  dividend = property(get_dividend)
  
  def get_split_coef(self):
    return float(self._split_coef)
  split_coef = property(get_split_coef)
  
a = Stock.INTRADAY('IBM', '5min')
#b = Stock.DAILY('IBM')
#c = Stock.DAILY_ADJUSTED('IBM')
#d = Stock.WEEKLY('IBM')
#e = Stock.WEEKLY_ADJUSTED('IBM')
f = Stock.MONTHLY('IBM')
g = Stock.MONTHLY_ADJUSTED('IBM')