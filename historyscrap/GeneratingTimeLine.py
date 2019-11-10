import pandas
import tldextract
from collections import Counter
import plotly.graph_objects as go
import plotly

def generateDomainChart(urlDomain):
    urlDataPresent = urlDomain.head(30)
    fig = go.Figure(data=[go.Bar(x=urlDataPresent['Domain'],y=urlDataPresent['Frequency'])])
    fig.update_layout(title_text="Domain visited",xaxis_title = "Domain",yaxis_title = "Frequency")
    plotly.offline.plot(fig, filename="Internet Domain History.html")
    #fig.show()

def generateBrowserTimeLineChart(dateDict,timeDict):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dateDict['Date'], y=dateDict['Frequency']))
    fig.add_trace(go.Scatter(x=timeDict['Time'], y = timeDict['Frequency'],visible = False))
    updatemenus = list([
        dict(active=-1,
             buttons=list([
                 dict(label='Day',
                      method='update',
                      args=[{'visible': [True, False]},
                            {'title': 'Browsing Activity',
                             'xaxis': {'title':'Date'},
                             }]),
                 dict(label='Time',
                      method='update',
                      args=[{'visible': [False, True]},
                            {'title': 'Browsing Time ',
                             'xaxis': {'title': 'Time (24-hour format)'}
                            }])
             ]),
             )
    ])

    fig.update_layout(updatemenus = updatemenus)
    fig.update_layout(title= "Browsing Activity",xaxis_title="Date",yaxis_title = "Frequency")
    plotly.offline.plot(fig, filename="Internet Activity.html")
    #fig.show()



def generateDomainData(df):
    URLdata = df['URL']
    URLdomainCounter = []
    for url in URLdata:
        tsd,td,tsu =tldextract.extract(url)
        if tsd != '' and tsd != 'www':
            URLdomainCounter.append(tsd+"."+td)
        else:
            URLdomainCounter.append(td)

    URLdomainCounter = Counter(URLdomainCounter)
    URLDomainCount ={}

    for website in URLdomainCounter:

        URLDomainCount[website] = URLdomainCounter[website]

    urlDomain = pandas.DataFrame(URLDomainCount.items(),columns=['Domain','Frequency'])
    urlDomain = urlDomain.sort_values(by=['Frequency'],ascending=False)
    generateDomainChart(urlDomain)

def generateBrowserTimelineData(df):

    dataf = pandas.DataFrame()
    data = df[df.DateTime != "1601-01-01 08:00:00"]

    dataf['DateTime'] = pandas.to_datetime(data['DateTime'])

    dateDF = pandas.DataFrame()

    dateDF['Date'] = [d.date() for d in dataf['DateTime']]
    dateDF['Time'] = dataf['DateTime'].dt.hour
    dateDict = {}
    for date in dateDF['Date']:

        if str(date) not in dateDict:
            dateDict[str(date)] = 1
        else:
            dateDict[str(date)] += 1
    timeDict = {}
    for time in dateDF['Time']:
        if time not in timeDict:
            timeDict[time] = 1
        else:
            timeDict[time] += 1

    dateGenerated = pandas.DataFrame(list(dateDict.items()), columns = ['Date','Frequency'])
    dateGenerated = dateGenerated.sort_values(by=['Date'])
    timeGenerated = pandas.DataFrame(list(timeDict.items()),columns = ['Time','Frequency'])
    timeGenerated = timeGenerated.sort_values(by=['Time'])
    generateBrowserTimeLineChart(dateGenerated,timeGenerated)
def setup():
    df = pandas.read_csv("general_history.csv")
    if not df.empty:
        generateDomainData(df)
        generateBrowserTimelineData(df)
