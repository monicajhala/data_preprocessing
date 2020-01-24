import pandas as pd
import numpy as np
from pymongo import MongoClient

data = pd.read_csv('lf_1_.csv',encoding='cp1252')
data = data[['Vendor']]

'''
for i in data.columns:
	print(i)

'''

client = MongoClient('mongodb://localhost:27017/Vendor_Data',connect=False)
mydb = client['Vendor_Data']
mycol = mydb['EKKO']
cursor = mycol.find()
df = pd.DataFrame(list(cursor))
df.columns = df.columns.str.replace(' ','')

df = df[['Vendor','Createdon','Purch-Doc-','Tot-value']]
df['Created on'] = df['Createdon']
df['Tot-value'] = df['Tot-value'].str.replace(',','')
df['Tot-value'] = df['Tot-value'].astype(float)

#df = df[:-1]
'''
df['Created on'] = df['Created on'].astype(str)
#print(df['Created on'].str[:2]+'-'+df['Created on'].str[3:5]+'-'+df['Created on'].str[6:])
df['Created on'] = df[df['Created on']!='None']
#df['Created on']= df['Created on'].str[:3]+'-'+df['Created on'].str[3:5]+'-'+df['Created on'].str[6:]
print(df['Created on'])
#df['created'] =pd.to_datetime(df['Created on'])
#print(df['created'])
'''

df['Created on'] = df['Created on'].astype(str)
df['Created on'] = df['Created on'].str[:2]+'-'+df['Created on'].str[3:5]+'-'+df['Created on'].str[6:]
#df['Created on'] = df['Created on']
#df['Created on'] = pd.to_datetime(df['Created on'])
df['Createdon'] = df['Created on']
df = df[df.Createdon.str[0] != 'N']
#print(df['Createdon'][10:30])
#print(df['Createdon'].str.len())
df = df[df['Createdon'].str.len() == 10]
df['Createdon'] = pd.to_datetime(df['Createdon'])
#print((df['Created on'][df['Created on']!='No-e']))


mer = pd.merge(data,df, on = 'Vendor', how='left')
mer.to_csv('vendorwithpurchase.csv')
print('__________________________________________________________________________')
print(mer.head(10))
print(mer.shape[0])

mer['Year'] = mer['Createdon'].dt.year
mer['Year'] = mer['Year'].fillna(0)
mer['Year'] = mer['Year'].astype(int)


mer['Month'] = mer['Createdon'].dt.month
mer['Month'] = mer['Month'].fillna(0)
mer['Month'] = mer['Month'].astype(int)

mer['Quarter'] = mer['Createdon'].dt.quarter
mer['Quarter'] = mer['Quarter'].fillna(0)
mer['Quarter'] = mer['Quarter'].astype(int)
#print(mer)
mer['Finical_Year'] = np.where(mer['Month'] <=3 , mer['Year']-1, mer['Year'])
conditions=[(mer['Month']==1),(mer['Month']==2),(mer['Month']==3),(mer['Month']==4),(mer['Month']==5),(mer['Month']==6),(mer['Month']==7),(mer['Month']==8),(mer['Month']==9),(mer['Month']==10),(mer['Month']==11),(mer['Month']==12)]
choice = [10,11,12,1,2,3,4,5,6,7,8,9]
mer['Finical_Month'] = np.select(conditions,choice)
mer = mer[mer['Year']!=0]
'''
conditions = [(mer['Finical_Month'] == 'APR') |(mer['Finical_Month'] == 'MAY')|(mer['Finical_Month'] == 'JUN'),(mer['Finical_Month'] == 'JUL') , (mer['Finical_Month'] == 'AUG')|(mer['Finical_Month'] == 'SEP')|(mer['Finical_Month'] == 'OCT')|(mer['Finical_Month'] == 'No' |]
mer = mer[mer['Year']!=0]
print(mer)
'''
'''
mer1 = mer
mer1['Count'] = 1
mer1 = mer1.groupby(['Finical_Year','Vendor'])['Purch-Doc-'].count()
mer1 = mer1.reset_index()
mer1 = pd.pivot_table(mer1,index='Vendor',values=['Purch-Doc-'],columns=['Finical_Year'])
mer1 = mer1.fillna(0)
print(mer1)
mer1.to_csv('mer1.csv')
'''

mer2 = mer
mer2['Count'] = 1
#mer2 = mer2[mer2.Finical_Year != 2016 | mer2.Finical_Year != 2015 ]
mer2 = mer2[mer2.Finical_Year != 2016]
mer2 = mer2[mer2.Finical_Year != 2015]
mer23 = mer2.groupby(['Finical_Year','Finical_Month','Vendor'])['Purch-Doc-'].count()
mer24 = mer2.groupby(['Finical_Year','Finical_Month','Vendor'])['Tot-value'].sum()


#mer21 = mer2.groupby(['Vendor'])
mer2 = mer23.reset_index()
mer3 = mer24.reset_index()
mer2 = pd.merge(mer2,mer3,on=['Finical_Year','Finical_Month','Vendor'])
print(mer2)
mer2 = mer2.sort_values(by = ['Finical_Year','Finical_Month'])
print(mer2.head(10))

mapp = {1:'01-APR',2:'02-MAY',3:'03-JUN',4:'04-JUL',5:'05-AUG',6:'06-SEP',7:'07-OCT',8:'08-NOV',9:'09-DEC',10:'10-JAN',11:'11-FEB',12:'12-MAR'}

mer2 = mer2.replace({'Finical_Month': mapp})
mer2 = pd.pivot_table(mer2,index='Vendor',values=['Purch-Doc-','Tot-value'],columns=['Finical_Year','Finical_Month'])

mer2 = mer2.fillna(0)
#mer2.to_csv('mer2.csv')

mer2 = mer2.reindex(sorted(mer2.columns),axis=1)
print(mer2)
mer2.to_csv('mer2.csv')
'''
mer3 = mer
mer3['Count'] = 1
mer3 = mer3.groupby(['Finical_Year','Finical_Month','Quarter','Vendor'])['Purch-Doc-'].count()
mer3 = mer3.reset_index()
print(mer3)
'''
