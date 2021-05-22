import pandas  as pd 
import plotly.express as px
import csv 

data=pd.read_csv('data.csv')
df=data.groupby(['student_id','level'],as_index=False)['attempt'].mean()
# print(df)
# level=df.loc[df['level']]
# print(level)

fig=px.scatter(df,x='student_id',y='level',color='attempt',size='attempt')
fig.show()
