# P1 for regression
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('demo.csv',index_col=0)

sns.pairplot(data=data,y_vars=['ABS'],x_vars=['Sales','ATV','Customers'],kind='reg')
plt.xlim(50,)
plt.ylim(1,)
plt.show()
plt.savefig("asd.png", bbox_inches="tight")


