import pprint
pp = pprint.PrettyPrinter(indent = 4)
print = pp.pprint

import requests, collections
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=0GGIM0L0U42EVGVN'

data = None
def _importData():
  _data = requests.get(url).json()
  print('Data imported successfully')
  return _data
  
print('Importing data...')
try:
  data = _importData()
except:
  print('Error importing data. Trying again...')
  data = _importData()

    
class stock():
  def __repr__(self):
    return self.__str__()
  
  def __str__(self):
    #return pp.pformat(self.__dict__)
    #return str(self.__dict__)
    dict = collections.OrderedDict()
    dict['ticker'] = self.ticker
    dict['interval'] = self.interval
    dict['interval_data']= "DATA LIST"
    
    return pp.pformat(dict)
    
    
  def __init__(self):
    self.ticker = None
    self.interval = None
    self.interval_data = []
  
  def Intraday(self, data):
    self.ticker = data['Meta Data']['2. Symbol']
    self.interval = data['Meta Data']['4. Interval']
    _intervals_key = 'Time Series (' + self.interval + ')'
    
    for key in list(data[_intervals_key].keys()):
      interval_data = data[_intervals_key][key]
      self.interval_data = [stock_interval(key, interval_data)] + self.interval_data

  def _dict(self):
    interval_list = []
    for interval in self.intervals:
      interval_list += [interval.dict()]
    return interval_list

class stock_interval():
  
  def dict(self):
    dict = collections.OrderedDict()
    dict['key'] = self._key,
    dict['open'] = self._open,
    dict['high'] = self._high,
    dict['low'] = self._low,
    dict['close'] = self._close,
    dict['volume'] = self._volume
    
    return dict
  
  
  def __init__(self, key, data):
    self._key = key
    self._open = data['1. open']
    self._high = data['2. high']
    self._low = data['3. low']
    self._close = data['4. close']
    self._volume = data['5. volume']
    
  def get_key(self):
    return self._key
    
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
    
  def get_volume(self):
    return int(self._volume)
  volume = property(get_volume)
  
  
a = stock()
a.Intraday(data)
a