import os
PATH="data/stock/year/"
#print(os.listdir(year_path))
for year in range(2000,2010):
    count=0
    year_path=os.path.join(PATH,str(year))
    for item in os.listdir(year_path):
        with open(os.path.join(year_path,item),"r") as f:
            #print(f.readline())
            f.readline()
            if f.readline()=="":
                #print(item)
                count+=1
    print("year {}: {} blank stock data".format(year,count))
    #break

