import pandas as pa
import plotly.express as px

df=pa.read_csv("C:/Users/Ezra/Desktop/Python/py/Data-visualization-master/Data-visualization-master/csv files/Copy+of+data+-+data.csv")
fig=px.scatter(df,x="date", y="cases",title="Amount of Cases Per Country",size_max=60, size="Percentage")
fig.show()