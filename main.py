#!/usr/bin/env python

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '*YOUR API KEY' #https://www.alphavantage.co/support/#api-key

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol='MSFT', outputsize = 'full') #enter your ticker of your choice symbol='TICKER'
close_data = data['4. close']
percentage_change = close_data.pct_change()
last_change = round((percentage_change[-1] * 100),2)

if abs(last_change) > 0.0004: #change volatality on your preference
    print('Alert: ' + str(last_change) + '%')
