import pandas as pd
import  numpy as np
from datetime import datetime, timedelta

data = pd.read_csv("data/cleaned_online_retail.csv")

# drop unnamed column
data = data.drop(["Unnamed: 0"], axis=1)

# convert order date to datetime
data['order_date'] = pd.to_datetime(data['order_date'])

data.info()

len(data['customer_id'].unique())

# aggregate data by customer id and compute frequency of purchase
customer_level_df = data[['customer_id', 'total_sale']] \
    .groupby('customer_id') \
        .agg({
                'total_sale': 'sum',
            }). reset_index()
        
customer_level_df['purchase_frequency'] = data.groupby('customer_id')['total_sale'].size().to_list()

customer_level_df['avg_revenue'] = customer_level_df['total_sale'] / customer_level_df['purchase_frequency']

customer_level_df['first_purchase_date'] = data.groupby('customer_id')['order_date'].min().to_list()

customer_level_df['last_purchase_date'] = data.groupby('customer_id')['order_date'].max().to_list()

customer_level_df.info()

#  calculate the time difference between first and last purchase in days

def calculate_customer_tenure(row):

    # Since the dates are already datetime objects, we can directly find the difference
    tenure = (row['last_purchase_date'] - row['first_purchase_date']).days
    
    return tenure

customer_level_df['customer_tenure'] = customer_level_df.apply(calculate_customer_tenure, axis=1)

customer_level_df