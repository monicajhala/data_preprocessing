import pandas as pd
import numpy as np

data = pd.read_csv('VendorMasterConcate.csv')
data['Count'] = 1
data1 = data
data = data.groupby(['Date','Time','Vendor','Field Name'])['Count'].sum()

data = data.reset_index()
print(data.shape[0])
'''
print(data)
data.to_csv('VC1.csv')
'''

data1['countvendor'] =1
data1 = data1.groupby(['Vendor'])['countvendor'].count()
data1 = data1.reset_index()
data1 = data1[['Vendor','countvendor']]
print(data1.shape[0])

mer = pd.merge(data,data1, on='Vendor')
print(mer)
mer.to_csv('VC2.csv')
