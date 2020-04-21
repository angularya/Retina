import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
#Date,TotalUp,TotalDown,Temp,Hum,WindSpd,Cloud,Desc
date = df['Date'].to_numpy()
totalUp = df['TotalUp'].to_numpy()
totalDown = df['TotalDown'].to_numpy()
Temperature = df['Temp'].to_numpy()
Humidity = df['Hum'].to_numpy()
WindSpeed = df['WindSpd'].to_numpy()
cloudiness = df['Cloud'].to_numpy()

layout = go.Layout(title='Plot from your Data')
fig = go.Figure(layout=layout)
fig.add_trace(go.Scatter(x=date,y=totalUp,
                    mode='lines+markers',
                    name='totalUp'))
fig.add_trace(go.Scatter(x=date, y=totalDown,
                    mode='lines+markers',
                    name='totalDown'))
fig.add_trace(go.Scatter(x=date, y=Temperature,
                    mode='lines+markers', name='Temperature'))
fig.add_trace(go.Scatter(x=date, y=Humidity,
                    mode='lines+markers', name='Humidity'))
fig.add_trace(go.Scatter(x=date, y=WindSpeed,
                    mode='lines+markers', name='WindSpeed'))
fig.add_trace(go.Scatter(x=date, y=cloudiness,
                    mode='lines+markers', name='cloudiness'))
fig.show()
