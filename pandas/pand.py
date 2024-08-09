import pandas as pd
import numpy as np
"""
num =[1,2,3,4]
strd=['a','n','c','n']
out = pd.Series(data=strd ,index= num)
print(out)
"""

df = pd.read_csv("income.csv")
print(df)

"""
col_name=df.columns
print("col_name", col_name[:2])
"""

#print(df[2:4])
#print(df.head(4))
#print(df.iloc[5])
#print(df.loc[])
#fil = df.filter(items=["State"])
#print(fil)

#u_value=df.index.unique()
#print(u_value)
#print(len(u_value))
#print(pd.crosstab(df.index,df.State))
#print(df.index.value_counts())
"""
print(df.sample(n=10))
data = df.sample(frac=0.1)
print(data)

zodic = pd.df({"Name":[]})
"""
#df["difference"] = df.Y2008 - df.Y2009
#print(df["difference"])

#df["difference"]=df.eval("Y2003-Y2002")
#print(df.head())
#groupby

#gr = df.groupby("State")['Y2002'].max()
#print(gr)


#filtering
"""
print(df[df.index=="A"])
print(df.loc[df.Index =="A"]) #All the col where Index is A
print(df.loc[df.Index=="A","State"])#only state col where index is A
print(df.loc[(df.loc =="A") & (df.Y2002>15000000),:])
print (df.loc[(df.Index=="A") | (df.index == "W"),:])
print("alternative", df.loc[df.Index.isin(["A","W"]),:])#prints were ever A and W is in index from entier dataset
"""

mydata ={'crop':["Rice","Millet","Wheat","Barley"],
'yield':[10101,1002,1002,1215],
 'cost':[102,np.nan,20,68]}
crops = pd.DataFrame(mydata)
print(crops)
#print(crops.isnull())
#print(crops.notnull())

#print("1",crops[crops.cost.isnull()].crop)
#print("2",crops[crops.cost.notnull()].crop)





















