import matplotlib.pyplot as plt
import numpy as np
from AlphaVantageP930 import *

plt.plot(a.index_double, a.lows2, label = 'low')
plt.plot(a.index_double, a.highs2, label = 'high')
plt.plot(a.index_double, a.opens_closes, label = 'open/close')
plt.plot(a.index_single, a.opens, label = 'open')
plt.plot([x+1 for x in a.index_single], a.closes, label = 'close')

plt.xlim(0,a.length)

plt.legend()

plt.xticks(a.index_single, a.keys, rotation = 90)

plt.grid()

plt.show()