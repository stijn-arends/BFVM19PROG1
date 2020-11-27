"""
This is a weather data collector script.
It collects every 60 seconds data from openweathermap
for each fetch a file is stored
"""

__author___ = 'Fenna Feenstra'

from urllib.request import urlopen
import os
import time
from twisted.internet import task, reactor

API_key = "9a4bd3520a281073413e444c8fda3a59"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_id = '2755250' # groningen
URL = base_url + "appid=" + API_key + "&id=" + city_id

def collect():
    ctime = time.strftime("%Y%m%d%H%M")
    JSON = "data/weatherfeed_{}.json".format(ctime)
    print("collecting data at ", ctime)
    if not os.path.exists(JSON):
        #write as bytes
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
try:
    l = task.LoopingCall(collect)
    l.start(60) # call every sixty seconds
    reactor.run()
except:
    print("too many requests")
finally:
    print("shutting down")
