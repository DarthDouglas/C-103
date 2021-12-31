import pandas as pa
import plotly.express as px

df=pa.read_csv("C:/Users/Ezra/Desktop/Python/py/Data-visualization-master/Data-visualization-master/Data.csv")
fig=px.scatter(df,x="date", y="cases",color="country",title="Amount of Cases Per Country")
fig.show()
