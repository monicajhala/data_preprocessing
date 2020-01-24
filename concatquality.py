import pandas as pd
import numpy as np

df = pd.read_csv('QALS_ECC..csv' , encoding = 'cp1252' )
df1 = pd.read_csv('QALS_ECC 2.csv', encoding = 'cp1252')
df2 = pd.read_csv('QALS_ECC 3.csv', encoding = 'cp1252')
df2 = pd.read_csv('QALS_ECC 3.csv', encoding = 'cp1252')
df3 = pd.read_csv('QALS_ECC 4.csv', encoding = 'cp1252')
df4 = pd.read_csv('QALS_ECC 5.csv', encoding = 'cp1252')
df5 = pd.read_csv('QALS_ECC 6.csv', encoding = 'cp1252')
# df6 = pd.read_csv('QALS 01.10.16 - 30.09.17 (2).csv')
# df7 = pd.read_csv('QALS 01.10.17 - 30.09.18.csv')
# df8 = pd.read_csv('QALS 01.10.18 - 30.09.19.csv')



concate = pd.concat([df,df1,df2,df3,df4,df5])
data = concate

data['Approval insp. lot'] = data['Approval insp. lot'].fillna(0)

data['Return to vendor'] = data['Return to vendor'].astype(str)
data['Return to vendor'] = data['Return to vendor'].str.replace(',','')
data['Return to vendor'] = data['Return to vendor'].astype(float)
conditions = [(data['Approval insp. lot']-data['Return to vendor'] == 0),(data['Approval insp. lot']-data['Return to vendor'] != 0)] 
choice = [1,4]
data['Approval. dev'] = np.select(conditions,choice)
data['Production Resource/Tool Saved for Insp.'] = data['Production Resource/Tool Saved for Insp.'].fillna(1)
data['Production Resource/Tool Saved for Insp.'] = data['Production Resource/Tool Saved for Insp.']
#data['Production Resource/Tool Saved for Insp.'] = data['Production Resource/Tool Saved for Insp.'].replace('X',0)
#print(data['Production Resource/Tool Saved for Insp.'])
#condition1 = [(data['Production Resource/Tool Saved for Insp.'] == 'X') & ()]

data['Production Resource/Tool Saved for Insp.1'] = np.where(data['Production Resource/Tool Saved for Insp.'] == 'X', 0, 1)
#print(data[['Production Resource/Tool Saved for Insp.','Production Resource/Tool Saved for Insp.1']])
condition1 = [(data['Production Resource/Tool Saved for Insp.1'] == 0) & (data['Return to vendor'] == 0), (data['Production Resource/Tool Saved for Insp.1'] == 0) & (data['Return to vendor'] != 0), (data['Production Resource/Tool Saved for Insp.1'] == 1) & (data['Return to vendor'] != 0)]
choice1 = [4,2,4]
data['Insp. dev'] = np.select(condition1,choice1)
#print(data[['Production Resource/Tool Saved for Insp.','Return to vendor','Insp. dev']][data['Insp. dev']==4])
data['Inspection stock'] = data['Inspection stock'].fillna(1)
data['Inspection stock1'] = np.where(data['Inspection stock'] == 'X',0,data['Inspection stock'])
#print(data['Inspection stock1'])
condition2 = [(data['Inspection stock1'] == 0) & (data['Return to vendor'] == 0),(data['Inspection stock1'] == 1) & (data['Return to vendor'] == 0),(data['Inspection stock1'] == 1) & (data['Return to vendor'] != 0),(data['Inspection stock1'] == 0) & (data['Return to vendor'] != 0) ]
choice2 = [4,2,4,2]
data['stock dev.'] = np.select(condition2,choice2)
data = data.groupby(['Vendor'])[['Approval insp. lot','Production Resource/Tool Saved for Insp.1','Inspection stock1','Return to vendor','Approval. dev','Insp. dev','stock dev.']].mean()
data.to_csv('quality_ranking_final.csv')

'''
data['Vendor'] = data['Vendor'].fillna(0)
data = data[data['Vendor']!=0]
print(data.shape[0])
data.to_csv('quality_ranking.csv')

data1 = pd.read_csv('/root/A/Mongo/final12.csv')
print(data1.shape[0])	

data1['Purchasing Document'] = data1['Purch-Doc-']
mdata = pd.merge(data,data1,on='Vendor', how='left')

#mdata.to_csv('asdf.csv')
'''
