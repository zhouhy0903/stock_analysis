import baostock as bs
import pandas as pd
import time
import os

class stock:
    STOCK_INFO="data/stock_info.csv"
    STOCK_MIN="data/stock/year"
    def __init__(self):

        if not os.path.exists(self.STOCK_MIN):
            os.makedirs(self.STOCK_MIN)


    def get_stock_year(self,stock_id,year):
    
        SAVE_PATH=os.path.join(self.STOCK_MIN,str(year))
        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)


        STARTDATE=str(year)+"-01-01"
        ENDDATE=str(year)+"-12-31"
        #print(STARTDATE,ENDDATE)
        print("---get {} data from {} to {}---".format(stock_id,STARTDATE,ENDDATE))
        try:
            lg = bs.login()
            print('login respond error_code:'+lg.error_code)
            print('login respond  error_msg:'+lg.error_msg)
            # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
            # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
            rs = bs.query_history_k_data_plus(code=stock_id,fields="date,time,code,open,high,low,close,volume,amount,adjustflag",
            start_date=STARTDATE, end_date=ENDDATE,
            frequency="5", adjustflag="3")
            print('query_history_k_data_plus respond error_code:'+rs.error_code)
            print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

            data_list = []
            while (rs.error_code == '0') & rs.next():
                data_list.append(rs.get_row_data())
            result = pd.DataFrame(data_list, columns=rs.fields)
            result.to_csv(SAVE_PATH+"/"+str(stock_id)+"-"+str(year)+".csv", index=False)
            print(result)
            bs.logout()
        except:
            pass
        time.sleep(0.5)


    def start(self):
        stock_info=pd.read_csv(self.STOCK_INFO,index_col=0)
        print(len(stock_info))
        for i in range(2003,2021):
            for st in stock_info["ts_code"]:
                stock_id=st[-2:].lower()+"."+st[:-3]
                self.get_stock_year(stock_id,i)
                print(stock_id)

            time.sleep(10)


mystock=stock()
mystock.start()

