# analysis2/analysis2.py

import matplotlib.pyplot as plt
import numpy as np

import tstools

timeseries = np.genfromtxt("./data/hotwire.csv", delimiter=",")
print ('Mean value: ', tstools.get_mean_and_var(timeseries)[0])
