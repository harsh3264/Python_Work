import numpy as np
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ages = np.random.gamma(6,3, size=50)
data = pd.read_csv('demo.csv')

sns.pairplot(data=data,
                  x_vars=['ABS'],
                  y_vars=['Sales', 'ABV'])
plt.savefig("chess.png", bbox_inches="tight")  