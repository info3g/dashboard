import pandas as pd 
import plotly.plotly as py
from plotly import graph_objs as go

dfObj = pd.DataFrame(data=df, columns = ['employer' , 'CreatedDate', 'RecommendationTitle'])
cDate = df['CreatedDate'][0]
date = str(cDate)[:4]
print(date)

firstQs = dfObj[dfObj['CreatedDate'] > date +'-01-01 00:00:00']
firstQ = firstQs[firstQs['CreatedDate'] < date +'-04-01 00:00:00']

secondQs = dfObj[dfObj['CreatedDate'] > date +'-04-01 00:00:00']
secondQ = secondQs[secondQs['CreatedDate'] < date +'-07-01 00:00:00']

thirdQs = dfObj[dfObj['CreatedDate'] > date +'-04-07 00:00:00']
thirdQ = thirdQs[thirdQs['CreatedDate'] < date +'-10-01 00:00:00']

fourthQs = dfObj[dfObj['CreatedDate'] > date +'-04-10 00:00:00']
fourthQ = fourthQs[fourthQs['CreatedDate'] < date +'-12-31 00:00:00']

print("Original Dataframe" , firstQ, sep='\n')

##### First Quarter  ######

firstQuarter = firstQ['RecommendationTitle']
first_1 = []
first_2 = []
first_3 = []
first_4 = []
nan_level = []
for level in firstQuarter:
  if str(level) == 'Strongly Not Recommended':
    first_1.append(level)
  elif str(level) == 'Not Recommended':
    first_2.append(level)
  elif str(level) == 'Recommended':
    first_3.append(level)
  elif str(level) == 'Highly Recommended':
    first_4.append(level)
  else:
    nan_level.append(level)
# print(level_4)
##### Second Quarter  ######
secondQuarter = secondQ['RecommendationTitle']
second_1 = []
second_2 = []
second_3 = []
second_4 = []
nan_level = []
for level in secondQuarter:
  if str(level) == 'Strongly Not Recommended':
    second_1.append(level)
  elif str(level) == 'Not Recommended':
    second_2.append(level)
  elif str(level) == 'Recommended':
    second_3.append(level)
  elif str(level) == 'Highly Recommended':
    second_4.append(level)
  else:
    nan_level.append(level)
    
######## Third Quarter ##########    
thirdQuarter = thirdQ['RecommendationTitle']
third_1 = []
third_2 = []
third_3 = []
third_4 = []
nan_level = []
for level in thirdQuarter:
  if str(level) == 'Strongly Not Recommended':
    first_1.append(level)
  elif str(level) == 'Not Recommended':
    first_2.append(level)
  elif str(level) == 'Recommended':
    first_3.append(level)
  elif str(level) == 'Highly Recommended':
    first_4.append(level)
  else:
    nan_level.append(level)
    
###### Fourth Quarter ###########    
fourthQuarter = fourthQ['RecommendationTitle']
fourth_1 = []
fourth_2 = []
fourth_3 = []
fourth_4 = []
nan_level = []
for level in fourthQuarter:
  if str(level) == 'Strongly Not Recommended':
    first_1.append(level)
  elif str(level) == 'Not Recommended':
    first_2.append(level)
  elif str(level) == 'Recommended':
    first_3.append(level)
  elif str(level) == 'Highly Recommended':
    first_4.append(level)
  else:
    nan_level.append(level)    

title = ['Jan-Mar(Q1)', 'Apr-June(Q2)', 'Jul-Sep(Q3)','Oct-Dec(Q4)' ]
data=[
    go.Bar(name='Strongly Not Recommended', x=title, y=[len(first_1),len(second_1),len(third_1),len(fourth_1)]),
  go.Bar(name='Not Recommended', x=title, y=[len(first_2),len(second_2),len(third_2),len(fourth_2)]),
  go.Bar(name='Recommended', x=title, y=[len(first_3),len(second_3),len(third_3),len(fourth_3)]),
  go.Bar(name='Highly Recommended', x=title, y=[len(first_4),len(second_4),len(third_4),len(fourth_4)]),
]

fig = go.Figure(data)
fig.layout.update(barmode='stack')
periscope.plotly(fig)