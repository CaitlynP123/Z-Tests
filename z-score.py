import statistics
from numpy import mean
import pandas as pd
import random 
import plotly.figure_factory as pf
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/C/OneDrive/Desktop/Coding/python/Normal Distribution/medium_data.csv")
data = df['reading_time'].tolist()

popMean = statistics.mean(data)
popStdDev = statistics.stdev(data)

print('Mean of Population Data = ', popMean)
print('Standard Deviation of Population Data = ', popStdDev)

def randSetMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

meanlist = []

for i in range(0, 1000):
    setofmeans = randSetMean(100)
    meanlist.append(setofmeans)
mean = statistics.mean(meanlist)
print('Mean of Sampling Distribution = ', mean)
  
stdDev = statistics.stdev(meanlist)
print('Standard Deviation of Sampling Distribution = ', stdDev)

std1start, std1end = popMean - stdDev, popMean + stdDev
std2start, std2end = popMean - (stdDev * 2), popMean + (stdDev * 2)
std3start, std3end = popMean - (stdDev * 3), popMean + (stdDev * 3)

def showDistPlot():
    fig = pf.create_distplot([meanlist], ['reading_score'], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode='lines', name='MEAN'))
    fig.add_trace(go.Scatter(x=[std2end, std2end], y=[0, 0.17], mode='lines', name='Standard Deviation 2 end'))
    fig.add_trace(go.Scatter(x=[std3end, std3end], y=[0, 0.17], mode='lines', name='Standard Deviation 3 end'))
    fig.add_trace(go.Scatter(x=[std2start, std2start], y=[0, 0.17], mode='lines', name='Standard Deviation 2 start'))
    fig.add_trace(go.Scatter(x=[std3start, std3start], y=[0, 0.17], mode='lines', name='Standard Deviation 3 start'))
    fig.show()

showDistPlot()

