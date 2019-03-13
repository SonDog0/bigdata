import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.python.autograph.pyct import anno

son = pd.read_csv('c:/java/ddrdata/cor_anal.csv')

print(son)

plt.figure(figsize=(12,12))
cor = son.corr()

sns.heatmap(cor ,annot=True , cmap = 'RdBu')

plt.show()

