import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import os
matplotlib.use('TkAgg')
plt.style.use("ggplot")

PATH="data/stock/year/"
print("enter the year:")
year=input()
print("enter the stock_id:")
stock_id=input()
if stock_id[:2]=="60":
    stock_id="sh."+stock_id+"-"+year+".csv"
else:
    stock_id="sz."+stock_id+"-"+year+".csv"
stock_path=os.path.join(PATH,year,stock_id)
stock_data=pd.read_csv(stock_path)
plt.plot(stock_data.index.tolist(),stock_data["close"].tolist())


plt.show()


