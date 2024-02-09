import pandas as pd
import numpy as np

data = pd.read_csv('data/OnlineRetail_utf8.csv')

data.info()

## Cleaning & Preprocessing
# Fix Data Types
data['InvoiceDate'] = data["InvoiceDate"].astype('datetime64[ns]')
data['CustomerID']  = data['CustomerID'].astype('Int64')
data['CustomerID']  = data['CustomerID'].astype('object')

data.info()

## Remove rows where customer ID is null
data.isnull().sum()

data = data.dropna(subset="CustomerID")

data.info()

## Clean column names
column_names = {
    "InvoiceNo": 'invoice_no',
    "StockCode": 'stock_code',
    "Description": 'description',
    "Quantity": 'quantity',
    "InvoiceDate": 'order_date',
    "UnitPrice": 'unit_price',
    "CustomerID": "customer_id",
    "Country": 'country'
    }

data.columns = data.columns.map(column_names)
data

data = data[['order_date',"customer_id",'invoice_no',"quantity", "unit_price", "stock_code","description", "country"]]

# Save Data
data.to_csv("data/cleaned_online_retail.csv", index=False)