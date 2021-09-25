import pandas as pd
import plotly.graph_objects as pe
data=pd.read_csv("data 2.csv")
# []
# group=data.groupby("level")["attempt"].mean()
# print(group)
# fig=pe.Figure(pe.Bar(x=group,y=["Level 1","Level 2","Level 3","Level 4"],orientation="h"))
# fig.show()
student=data.loc[data["student_id"]=="TRL_imb"]
level4=student.loc[student["level"]=="Level 4"]
group=student.groupby("level")["attempt"].mean()
print(group)
fig=pe.Figure(pe.Bar(x=group,y=["Level 1", "Level 2", "Level 3", "Level 4"],orientation="h"))
fig.show()