import pandas  as pd 
import plotly.express as px
import csv 

data=pd.read_csv('data.csv')
df=data.groupby('level')['attempt'].mean()
print(df)

fig=px.scatter(x=df,y='level',color='attempt',size='level')
fig.show()