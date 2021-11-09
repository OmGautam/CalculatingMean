import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd 
import csv
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def randomSetMean(counter):
    dataSet = []
    for i in range(0,counter):
        rand = random.randint(0,len(data))
        value = data[rand]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setUp():
    meanList = []
    for i in range(0,100):
        setOfMeans = randomSetMean(30)
        meanList.append(setOfMeans)
    showFig(meanList)

setUp()




