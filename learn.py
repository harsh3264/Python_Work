import warnings
warnings.filterwarnings("ignore") # To remove all the warnings
import pandas as pd # Pandas library call
import numpy as np # numpy lib
import seaborn as sns # seaborn module
import matplotlib.pyplot as plt # generate the graph
from sklearn.cross_validation import train_test_split # Machine learning came into the picture scikit library
from sklearn.linear_model import LinearRegression # Import linear regression
from sklearn import metrics
from math import sqrt  # import metrics to calculate the Root mean square Error (RMSE) value

data = pd.read_csv('names.csv') # panda will read the csv file
data.index = np.arange(1,len(data)+1) # set the index as 1, if column 1 of data set is index then set index_col = 0 

feature_cols = ['Sales','ABS','Customers'] # Create a list which contains all the required X axis values
 
X = data[feature_cols]
y = data.ATV # Y axis only contains one value and it is an int that's why direct data.sales

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1) # split up the data set into training and testing data 

# To check the splits use print X_train.shape, print y_test.shape. Shape is used to check the split. By default split is 75 to 25

linreg = LinearRegression() # Instantiate the model

linreg.fit(X_train,y_train) # Use it to fit our training data set into the lg. Usually to learn the coeficients of the data set

print linreg.intercept_ # To check the intial static value of the linear reg formula 
print linreg.coef_ # Calculate the coefcient of respective X axis value in the formula

print zip(feature_cols, linreg.coef_) # For each value know the coef

# Our output is intercept = 111.601580632
 
# Coeficient for each [('Sales', 0.0053079013894121712), ('ABS', 0.86418006271355396), ('Customers', -0.80495798629484006)]

# Formula is y = 111.6015 + (0.00530 * Sales) + (0.86418 * ABS) + (-0.80495 * Customers)
# Formula contains one negative value which means that column is not useful for our dataset. We will prove this further
# To check the graph use this command the seaborn lib with matplotlib --> sns.pairplot(data=data,y_vars=y,x_vars=X,kind='reg'), plt.show

y_pred = linreg.predict(X_test) # Make prediction on the testing test

print np.sqrt(metrics.mean_squared_error(y_test,y_pred)) # RMSE value for the test set and the predicted value

# Output is 22.14 which means this method has not useful featured column. 
# If the value --> [0,2] that means the values taken in the X axis are meaningful
# In our data set taking customer does not make any sense
# Instead of Customers we can take Qty or Bills to check the results. If error is still greater than range change the model
# If still no change then that means only Sales and ABS are useful for this dataset 

