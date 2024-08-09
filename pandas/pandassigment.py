import pandas as pd
import numpy as np

df = pd.read_csv("iris.csv")
print(df)

#print(df[:10])
#print("datatype",df.dtypes)
#print("sumarrize", df.describe())
#print("mean",df["Sepal.Length"].mean)
#u_values = df.loc[df["Sepal.Length"]>5.0]
#print(df.loc[df.Species=="setosa"])

#print(df["Petal.Length"].agg(["mean","median","std"]))
#print(df.groupby("Species").count())
#print(df["Petal.Width"].agg(["min","max"]))

#print("average",df["Sepal.Width"].mean())

#df.ratio = df["Petal.Length"]/df["Petal.Width"]
#print(df.ratio)

#print(df.groupby("Species").df["Sepal.Length"].agg(["25%","50%","75%"]))
mi=print(df.groupby("Species")["Petal.Length"].min())
ma=print(df.groupby("Species")["Petal.Length"].max())

print("differnce",(ma-mi))

#df_habitat= pd.Dataframe({
    #'habitat'['forst','grassland','']
#})














