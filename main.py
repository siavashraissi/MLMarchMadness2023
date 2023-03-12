import numpy as np
import pandas as pd
import sklearn
import seaborn as sb 
import matplotlib.pyplot as plt

mm = pd.read_csv("cbb21.csv")
mm = mm.dropna(axis = 0)
corrM = mm.corr()
sb.heatmap(corrM, cmap = "Reds")

plt.show()