import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import datetime
from plot_class import *

api_key = "dk6g1w736tm81f51qhr9re"

#current timestamp is proper format
def stampNow():
    return datetime.now().timestamp()
#value like timestamp equal to 1 hour
def hourStamp():
    return 3600

#value like timestamp equal to 1 day
def dayStamp():
    return hourStamp()*24

class CryptPlot(Plot):
    def __init__(self):
        super(CryptPlot, self).__init__()
        
class CurrencyStats:
    def __init__(self):
        pass

#got request? nice - feed it here. This function fills class with fields that i considered to be <useful>    
def getCurrencyStatsByResponse(response):
    time_stamps = response.json()['data'][0]['timeSeries']
    #candle stats
    def getCandle(time_stamp):
        return time_stamp['open'], time_stamp['close'], time_stamp['low'], time_stamp['high'],\
            time_stamp['volume']
    #get basic scores of plot
    
    stats = CurrencyStats()

    stats.opens = CryptPlot()
    stats.closes = CryptPlot()
    stats.lows = CryptPlot()
    stats.highs = CryptPlot()
    stats.volume = CryptPlot()
    
    stats.reddit_scores = CryptPlot()
    stats.social_scores = CryptPlot()
    stats.soc_impact = CryptPlot()
    stats.news_data = CryptPlot()
    stats.galaxy_scores = CryptPlot()
    stats.market_cap = CryptPlot()
    
    for i in range(len(time_stamps)):
        candle = getCandle(time_stamps[i])

        timestamp = time_stamps[i]['time']
        dt_object = datetime.fromtimestamp(timestamp)

        stats.opens.addPoint(candle[0])
        stats.closes.addPoint(candle[1])
        stats.lows.addPoint(candle[2])
        stats.highs.addPoint(candle[3])
        stats.volume.addPoint(candle[4])
        
        time_stamp = time_stamps[i]
        
        #cosials
        stats.reddit_scores.addPoint(time_stamp['reddit_posts_score'])
        stats.social_scores.addPoint(time_stamp['social_score'])
        stats.soc_impact.addPoint(time_stamp['social_impact_score'])
        stats.news_data.addPoint(time_stamp['news'])
        stats.galaxy_scores.addPoint(time_stamp['galaxy_score'])
        stats.market_cap.addPoint(time_stamps[i]['market_cap'])
        
    return stats


#generate request address by api key; data points (in hours) and end point
def gen_request_str(currency, endPoint, data = 'assets', data_points = 100):
    return 'https://api.lunarcrush.com/v2?data='+str(data)+'&key='+api_key+'&symbol='+str(currency)+\
        '&data_points='+str(data_points)+'&end='+str(endPoint)

#perform request
def getStats(currency, data_points = 100, endPoint = stampNow()):
    response = requests.get(gen_request_str(currency, endPoint = endPoint, data_points=data_points))
    if response.status_code == 200:
        print('Got it')
    elif response.status_code == 404:
        print('WRONG REQUEST')
    return response

#kind of useless stuff but i don't want to delete it
def getCurrencyStats(currency, data_points = 100, endPoint = stampNow()):
    response = getStats(currency, data_points = data_points, endPoint = endPoint)
    return getCurrencyStatsByResponse(response)