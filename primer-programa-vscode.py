print("Hola mundo")
import numpy as np
import plotly.graph_objects as go
import plotly 
print(plotly.__version__)

t=np.arange(0,1,0.01)
f1=np.sin(2*np.pi*t)
f2=np.cos(2*np.pi*t)

fig=go.Figure()
fig.add_trace(go.Scattergl(x=t,y=f1,mode="lines",name="Sseno"))
fig.add_trace(go.Scattergl(x=t,y=f2,mode="lines",name="Coseno"))
fig.add_trace(go.Scattergl(x=t,y=f1+f2,mode="lines",name="Suma"))
fig.show()
