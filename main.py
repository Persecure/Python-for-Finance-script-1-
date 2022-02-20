#!/usr/bin/env python
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'G1YYB1C7PQZDIAYM'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='MSFT', outputsize = 'full')
close_data = data['4. close']
percentage_change = close_data.pct_change()
last_change = round((percentage_change[-1] * 100),2)
if abs(last_change) > 0.0004:
    print('Alert: ' + str(last_change) + '%')
