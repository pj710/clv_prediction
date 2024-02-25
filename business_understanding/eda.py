import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns

data = pd.read_csv("data/cleaned_online_retail.csv")

data

data.info()

## Correct datatypes
data["order_date"] =  pd.to_datetime(data["order_date"])
data['customer_id'] = data['customer_id'].astype("object")

data['total_sale'] = data['quantity'] * data['unit_price']

# remove rows where quantity is less than 0
data_cleaned = data[data['quantity'] > 0]

data_cleaned

summary_stats_numeric = data_cleaned.select_dtypes('number'). describe()

summary_stats_categorical = data_cleaned.select_dtypes('object').describe()

## Explore numeric distributions
fig, ax =  plt.subplots(2,2, figsize=(10,12))

ax[0,0].hist(x = np.log(data_cleaned['quantity'] + 1), bins = 50)
ax[0,1].hist(x = np.log(data_cleaned['unit_price'] + 1), bins = 50)
ax[1,0].hist(x = np.log(data_cleaned['total_sale'] + 1), bins  = 50) 

# Formatting
ax[0,0].set_title("Quantity (Log)", fontweight="bold")
ax[0,1].set_title("Unit Price(Log)", fontweight="bold")
ax[1,0].set_title("Total Sale(Log)", fontweight="bold")

## Explore catergorical Distributions

data_cleaned.to_csv('data/cleaned_online_retail.csv')