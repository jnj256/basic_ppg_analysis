import os
from process_ppg import load_PPG_signal, get_filtered_ppg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# see this later
# https: // towardsdatascience.com/preprocessing-iot-data-linear-resampling-dde750910531

filepath = r'..\data\RawPPG\s001\ppgSignal_high_2021-03-13 193321.748690.csv'

raw_signal, tElapsed = load_PPG_signal(filepath)
sample_rate = 30.0

tElapsed_new = []
tElapsed_new.append(0)
max_time = 0
for idx in range(len(tElapsed) - 1):
	diff = tElapsed[idx+1] - tElapsed[idx]
	if diff <= 2.5*(1.0/sample_rate):
		max_time = max_time + diff
	else:
		print('diff', diff)
		print('max_time_before', max_time)
		max_time = max_time + (1.0/sample_rate)
		print('max_time_after', max_time)
	tElapsed_new.append(max_time)

tElapsed_new = np.asarray(tElapsed_new)

plt.plot(tElapsed_new, raw_signal)
plt.show()

series = pd.Series(raw_signal, pd.DatetimeIndex(tElapsed_new*1000000))
# series

tmp = pd.to_timedelta(series)
tmp.head()
exit()

tmp = series.resample('33.33ms')
# tmp.
# print(type(tmp))

resampled = tmp.to_numpy()
plt.plot(resampled)
plt.show()

# filtered = get_filtered_ppg(raw_signal, sample_rate=sample_rate)
