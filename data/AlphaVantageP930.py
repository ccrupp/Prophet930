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
    dict['ticker'] = self._ticker
    dict['interval'] = self._interval
    dict['length'] = self._length
    dict['interval_data']= "DATA LIST"
    
    return pp.pformat(dict)
    
    
  def __init__(self):
    self._ticker = None
    self._interval = None
    self._interval_data = []
    self._length = 0
  
  def Intraday(self, data):
    self._ticker = data['Meta Data']['2. Symbol']
    self._interval = data['Meta Data']['4. Interval']
    _intervals_key = 'Time Series (' + self._interval + ')'
    
    for key in list(data[_intervals_key].keys()):
      interval_data = data[_intervals_key][key]
      self._interval_data = [stock_interval(key, interval_data)] + self._interval_data
      
    self._length = len(self._interval_data)

  def _dict(self):
    interval_list = []
    for interval in self.intervals:
      interval_list += [interval.dict()]
    return interval_list
    
  def get_ticker(self):
    return self._ticker
  ticker = property(get_ticker)
  
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
  
  def get_opens(self):
    open_list = []
    for interval in self._interval_data:
      open_list += [interval.open]
    return open_list
  opens = property(get_opens)

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
  
  def get_closes(self):
    close_list = []
    for interval in self._interval_data:
      close_list += [interval.close]
    return close_list
  closes = property(get_closes)
  
  def get_volumes(self):
    volume_list = []
    for interval in self._interval_data:
      volume_list += [interval.volume]
    return volume_list
  volumes = property(get_volumes)
  
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
    
  def get_volume(self):
    return int(self._volume)
  volume = property(get_volume)
  
  
a = stock()
a.Intraday(data)
a