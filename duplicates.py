import pandas as pd 
#df = pd.read_csv("World_lfa1.csv",encoding='cp1252', header= 0, delim_whitespace= 'True')
df = pd.read_csv('World_lfa1.csv',encoding = 'cp1252')
print(df.head(20))
df['count'] = 0
df1 = df.groupby(['Vendor'])['count'].count()
df1 = df1.reset_index()
print(df1)
df1.to_csv("duplicates.csv")

