import pandas as pd 
df = pd.read_csv("for_caseid1.csv")
import datetime



#df['time:timestamp'] =  pd.to_datetime(df['time:timestamp'], format='%d-%m-%Y')
#print(df)

for i in df.columns:
	print(i)

'''
df1 = df[df['time:timestamp'].str[2] == '.']
#print(df1)
df2 = df[df['time:timestamp'].str[2] == '-']
#print(df2)
df3 = df[df['time:timestamp'].str[2] == '/']
#print(df3)
df1['time:timestamp'] = df1['time:timestamp'].str[:2]+'-'+df1['time:timestamp'].str[3:5]+'-'+df1['time:timestamp'].str[6:]
df1['time:timestamp'] = pd.to_datetime(df1['time:timestamp'])
print(df1)
df2['time:timestamp'] = df2['time:timestamp'].str[:2]+'-'+df2['time:timestamp'].str[3:5]+'-'+df2['time:timestamp'].str[6:]
#df3['time:timestamp'] = df3['time:timestamp'].str[3:5]+'-'+df3['time:timestamp'].str[:2]+'-'+df3['time:timestamp'].str[6:]
df2['time:timestamp'] = pd.to_datetime(df2['time:timestamp'])
print(df2)
df3['time:timestamp'] = pd.to_datetime(df3['time:timestamp'])
print(df3)
listof = [df1,df2,df3]
data = pd.concat(listof)
print(data)
print(df.shape[0])
'''
data = pd.read_csv('/root/A/supply_chain/celonis_data.csv')
print(data.columns)

df1 = data[['Vendor_x','Created on']]
df1['date'] = df1['Created on']
df1['concept_name'] = 'PO created'
df1 = df1[['Vendor_x','date','concept_name']]
print(df1)
df2 = data[['Vendor_x','Changed On']]
df2['concept_name'] = 'PO changed'
df2['date'] = df2['Changed On']
df2 = df2[['Vendor_x','date','concept_name']]
df3 =data[['Vendor_x','Document Date']]
df3['concept_name'] = 'Invoice'
df3['date'] = df3['Document Date']
df3 = df3[['Vendor_x','date','concept_name']]
listof = [df1,df2,df3]
data2 = pd.concat(listof)
print(data2.columns)
#data2.to_csv('caseid_1.csv')


