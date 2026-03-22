# The task is to multiply the track in new.gpx
# to repeat on consecutive days to sum up to enough kilometers to replace this: https://www.strava.com/activities/6139982714
# TODO BEFORE DOING ANYTHING ELSE check - maybe we can pinpoint where the meter broke and can insert kilometers there instead of
    # making up shit in July.
# TODO copy every day zip-style by enumerating the first day and appending a copy with altered day to the N-th day
# TODO Add additional 3 days in August - copypaste from July, but 

import os
import xml.etree.ElementTree as ET
from dateutil import parser
from datetime import datetime as dt

ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
# print(os.chdir("Downloads"))

with open("new_modified.gpx", 'r') as xmlfile:
    xmldata = ET.parse(xmlfile)
    data = xmldata.getroot()

for n in range(1, 31):
    data[1].append(data[1][2])
    for item in enumerate(data[1][2]): # TODO 
        timestampstr = item[1].text
        timestamp = parser.parse(timestampstr)
        timestamp = timestamp.replace(day=daynumber)
        item[1].text = timestamp.isoformat()

for n in range(1, 4): 


xmldata.write("final.gpx")
