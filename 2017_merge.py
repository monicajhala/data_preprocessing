import pandas as pd 
df = pd.read_csv('final_121_weightages.csv')
for i in df:
	print(i)
# df = df[['Purch-Doc-','Del-Date','Sched-Qty_x','Delivered_x','Createdon','Quantity-deliver-percent_x','Quantity-Ranking_x','Del-Date1_x','Sched-Qty_y','Delivered_y','Quantity-deliver-percent_y','Quantity-Ranking_y','Createdon1','Del-Date1_y','Difference_in_days','material_delivery_date_ranking','NetPrice_final','Material_x','net_price_ranking','Purch.Doc.',
# Vendor
# CITY
# TAX NO. 3
# ADDRESS
# TITTLE
# URL_x
# gst_ranking
# URL_ranking
# temp
# temp1
# gst_title_ranking
# GST_CHAR
# Title_CHAR
# URL_CHAR
# net_price_deviation
# Approval insp. lot
# Return to vendor
# Defect. qty in IQty
# Production Resource/Tool Saved for Insp.1
# Approval. dev
# Insp. dev
# stock dev.
# net_price_deviation.1
# net_price_ratio
# net_price_ranking
# min_net_price
# Material
# Region_code
# TAX NO. 3.1
# TAX NO. 4
# find_gst
# regional_code
# regional_code1
# RG_ranking
# Approval. Dev
# Production Resource/Tool Saved for Insp.1.1
# Return to vendor.1
# Approval dev.
# Insp. dev.1
# stock dev..1
# active_block_vendors


# df1 = pd.read_csv("rseg 2017 1 series material ecc.csv",error_bad_lines= False,encoding='cp1252')
# df1 = df1[['Document Number','Purchasing Document']]
# df1['Purchasing Document'] = df1['Purchasing Document'].astype(str)
# # df1.to_csv('')
# df2 = pd.read_csv("rseg_2017.csv",error_bad_lines=False,encoding='cp1252')
# # for cols in df2.columns:
# 	# print(cols)
# df2 = df2[['DocumentNo','Purchasing Document']]
# # print(df2.shape)
# df2['Purchasing Document'] = df2['Purchasing Document'].astype(str)
# # df3 = pd.read_csv('')
# df3 = pd.read_csv("EKKO.csv",error_bad_lines=False,encoding='utf8')
# df3['Created_year'] = df3['Created on'].str[:-4]
# df3 = df3[df3.Created_year == '2017']
# df3['Purchasing Document'] = df3['Purch.Doc.']
# # print(df3.shape)
# # for cols in df3.columns:
# 	# print(cols)

# df4 = pd.merge(df1,df3,on= 'Purchasing Document',how = 'left')
# df5 = pd.merge(df2,df3,on= 'Purchasing Document',how = 'left')
# df6 = pd.concat([df4,df5])
# df6 = df6[['Purchasing Document','Document Number']]
# # print(df6)
# # df6.to_csv('invoice.csv')
# # print(df6.shape)
# df7 = pd.read_csv("final121.csv",encoding = 'cp1252')
# df7['Purchasing Document'] = df7['Purch-Doc-'].astype(str)
# df7['Created_year'] = df7['Createdon'].str[:-4]
# df7 = df7[df7.Created_year == '2017']
# df8 = df7[['Purchasing Document','Vendor']]

# # print(df8.shape)
# df9 = pd.merge(df6,df8, on = 'Purchasing Document', how = 'left')
# df9.to_csv("duplicates2.csv")
# print(df9.shape)







