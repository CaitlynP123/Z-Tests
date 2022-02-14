import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics
import pandas as pd

df = pd.read_csv('C:/Users/C/OneDrive/Desktop/Coding/python/Normal Distribution/medium_data.csv')
data = df['reading_time'].tolist()

def randSetMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0,100):
    setOfMeans = randSetMean(30)
    meanlist.append(setOfMeans)

stdDev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

print("Mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", stdDev)

firstStdDevStart, firstStdDevEnd = mean - stdDev, mean + stdDev
secondStdDevStart, secondStdDevEnd = mean - (2 * stdDev), mean + (2 * stdDev)
thirdStdDevStart, thirdStdDevEnd = mean - (3 * stdDev), mean + (3 * stdDev)

meanSample1 = statistics.mean(data)
print("Mean of sample 1:- ",meanSample1)

fig = ff.create_distplot([meanlist], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.8], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanSample1, meanSample1], y=[0, 0.8], mode="lines", name="sample 1 mean"))
fig.add_trace(go.Scatter(x=[firstStdDevEnd, firstStdDevEnd], y=[0, 0.8], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[secondStdDevEnd, secondStdDevEnd], y=[0, 0.8], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[thirdStdDevEnd, thirdStdDevEnd], y=[0, 0.8], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - meanSample1) / stdDev
print("The z score is = ",z_score)