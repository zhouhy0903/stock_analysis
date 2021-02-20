import pandas as pd
import tushare as ts
ts.set_token("3a22661bc4b569596c2b936a5664e4cb828d771021404e5afa634955")
pro=ts.pro_api()
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
data.to_csv("data/stock_info.csv")
