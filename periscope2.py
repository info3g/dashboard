import plotly.plotly as py
from plotly import graph_objs as go

dfObj = pd.DataFrame(data=df, columns = ['employer' , 'CreatedDate', 'RecommendationTitle'])
try:
  fDate = df['CreatedDate'][0]
  ln = len(df['CreatedDate'])
  lDate = df['CreatedDate'][int(ln)-1]  
  month =		{1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct' ,11:'Nov',12:'Dec'}
  fdate = str(fDate).split(' ')
  fdate = fdate[0].split('-')
  fyear = fdate[0]
  fdate = int(fdate[1])
  first_date = "{} {}".format(month[fdate],fyear)
  print("First date : ",first_date)
  
  ldate = str(lDate).split(' ')
  ldate = ldate[0].split('-')
  lyear = ldate[0]
  ldate = int(ldate[1])
  last_date = "{} {}".format(month[ldate],lyear)
  print("Last date : ",last_date)
except:
  print("No Record found for this date range")

# print("Original Dataframe" , dfObj, sep='\n')

##### First Quarter  ######

firstQuarter = dfObj['RecommendationTitle']
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
 
## Titles need to change based on dynamic date field. 
title = ["{} - {}".format(first_date,last_date) ]
data=[
    go.Bar(name='Strongly Not Recommended', x=title, y=[len(first_1)]),
  go.Bar(name='Not Recommended', x=title, y=[len(first_2)]),
  go.Bar(name='Recommended', x=title, y=[len(first_3)]),
  go.Bar(name='Highly Recommended', x=title, y=[len(first_4)]),
]

fig = go.Figure(data)
fig.layout.update(barmode='stack')
periscope.plotly(fig)