import pandas as pd
from pymongo import MongoClient
import numpy as np

client = MongoClient('mongodb://localhost:27017/Vendor_Data',connect=False)
mydb = client['Vendor_Data']
mycol = mydb['EKKO']
mycol1 = mydb['EKET']


cursor = mycol.find()
df = pd.DataFrame(list(cursor))
df.columns = df.columns.str.replace(' ','')
df = df[['Purch-Doc-','Createdon','Vendor']]
print(df.head())
print('_______________')
cursor = mycol1.find()
df1 = pd.DataFrame(list(cursor))
df1.columns = df1.columns.str.replace(' ','')
#d1f = df1[['Purch-Doc-','Del-Date','Sched-Qty']]

df1 = df1[['Purch-Doc-','Del-Date','Sched-Qty','Delivered']]
data = pd.merge(df1,df, on = 'Purch-Doc-', how = 'left')
#data.to_csv('EKET-EKKO.csv')
print(data.columns)
data.columns = data.columns.str.replace(' ','')
data['Sched-Qty'] = data['Sched-Qty'].astype(str)
data['Delivered'] = data['Delivered'].astype(str)
data['Sched-Qty'] = data['Sched-Qty'].str.replace(',','')
data['Delivered'] = data['Delivered'].str.replace(',','')
'''
data['Delivered'] = data['Delivered'].str.replace('.00','')
print(data['Delivered'])
data['Sched-Qty'] = data['Sched-Qty'].str.replace('.00','')
'''
data['Delivered'] = np.where(data['Delivered'].str[:-3]=='.00',data['Delivered'].str[-3:],data['Delivered'])
data['Sched-Qty'] = np.where(data['Sched-Qty'].str[:-3]=='.00',data['Sched-Qty'].str[-3:],data['Sched-Qty'])
data['Delivered'] = data['Delivered'].astype(float)
data['Sched-Qty'] = data['Sched-Qty'].astype(float)
data['Quantity-deliver-percent'] = ((data['Delivered'] / data['Sched-Qty'])*100)
'''
data['Quantity-Ranking'] = np.select( [(data['Quantity-deliver-percent'] < 2 ) ,(data['Quantity-deliver-percent'] > =2) & (data['Quantity-deliver-percent'] <5),(data['Quantity-deliver-percent'] >= 5) & (data['Quantity-deliver-percent'] <= 9)],[1,2,3,4])
'''
conditions = [(data['Quantity-deliver-percent'] < 75),(data['Quantity-deliver-percent'] >=75) & (data['Quantity-deliver-percent'] < 84),(data['Quantity-deliver-percent'] >= 85) & (data['Quantity-deliver-percent'] <= 94), (data['Quantity-deliver-percent'] >=95) & (data['Quantity-deliver-percent'] == 100) ]
choice = [4,3,2,1]
data['Quantity-Ranking'] = np.select(conditions,choice)
data['Createdon'] = data['Createdon'].fillna(0)
print(data['Createdon'][:20])


data1 = data[data['Createdon'] != 0]
data1['Createdon1'] = data1['Createdon'].str[3:5] +'-'+data1['Createdon'].str[:3]+'-'+data1['Createdon'].str[6:]
data1['Createdon1'] = pd.to_datetime(data1['Createdon1'])

data['Del-Date1'] = pd.to_datetime(data['Del-Date'].str[3:5]+'-'+data['Del-Date'].str[:3]+'-'+data['Del-Date'].str[6:])
data1['Del-Date1'] = pd.to_datetime(data['Del-Date1'])


data1['Difference_in_days'] = (data1['Del-Date1']-data1['Createdon1'])/np.timedelta64(1, 'D')
data1['Difference_in_days'] = data1['Difference_in_days'].fillna(0)
data1['Difference_in_days'] = data1['Difference_in_days'].astype(int)

conditions = [(data1['Difference_in_days'] < 0),(data1['Difference_in_days'] > 0) & (data1['Difference_in_days'] < 10) , (data1['Difference_in_days'] >=10) & (data1['Difference_in_days'] < 20), (data1['Difference_in_days'] >=20) & (data1['Difference_in_days'] <30), (data1['Difference_in_days'] >= 30) ]
choice = [-1,1,2,3,4]

data1['material_delivery_date_ranking'] = np.select(conditions,choice)




finaldata  = pd.merge(data,data1, on=['Purch-Doc-','Del-Date','Createdon'], how = 'left')
print(finaldata.columns) 
finaldata = finaldata[['Vendor_x','Purch-Doc-','Del-Date','Sched-Qty_x','Delivered_x','Createdon','Quantity-deliver-percent_x','Quantity-Ranking_x','Difference_in_days','material_delivery_date_ranking']]
#finaldata1 = finaldata[['Vendor_x','Purch-Doc-','Quantity-Ranking_x','material_delivery_date_ranking']]
finaldata.to_csv('final_output.csv')
print(finaldata[['Quantity-Ranking_x','Quantity-deliver-percent_x']])
#print(data1)
#print(finaldata.head(100))


