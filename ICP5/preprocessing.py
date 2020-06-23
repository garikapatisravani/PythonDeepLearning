import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
train = pd.read_csv('train.csv') # Data set
# Scatter Plot before removing outlier
garage_area = train['GarageArea']
sales_price = train['SalePrice']
plt.scatter(garage_area, sales_price, alpha=1, color='r')
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('Before removing outliers')
plt.show()
# Removing outlier by using zscore , Z score is the relationship between MEAN and Standard Deviation.
data = pd.concat([train['GarageArea'], train['SalePrice']], axis=1)
z = np.abs(stats.zscore(data)) #calculate z-scores of `df`
new_df = data[(z < 2).all(axis=1)]
# Scatter Plot after removing outlier
garage_area = new_df['GarageArea']
sales_price = new_df['SalePrice']
plt.scatter(garage_area, sales_price, alpha=1, color='b')
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('After removing outliers')
plt.show()
