import pandas as pd
import numpy as np
data = pd.read_csv("India_lfa1.csv",encoding='cp1252')
data1 = pd.read_csv("final_121_weightages.csv",encoding='cp1252')
# data['Vendor1'] = data['Vendor'] 
# data = data[['Vendor','Vendor1']]
final_121_weightages = pd.merge(data1,data, on = 'Vendor', how = 'left')

#merdata.to_csv("merdata.csv")


# print(merdata).head()
# print(pd.data[['Vendor']].unique())

conditions = [(final_121_weightages['Vendor'] == final_121_weightages['active_block_vendors']),(final_121_weightages['Vendor'] != final_121_weightages['active_block_vendors'])]
choice = [1,4]
final_121_weightages['active_vendor_ranking'] = np.select(conditions,choice)
# for i in merdata.columns:
# 	print(i)
print(['active_vendor_ranking'])
# final_121_weightages.to_csv('/root/A/merdata.csv')
print(final_121_weightages.head())
