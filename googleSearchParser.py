#!/bin/python
import json
import os
from datetime import datetime, timedelta
from dateutil.parser import parse
from collections import OrderedDict

def readFile(filePath):
    jsonD = json.loads(open (filePath).read())
    return jsonD
    

def microsecondToDateTime(microsecond):
    epoch = datetime(1970, 1, 1)
    cookie_microseconds_since_epoch = int(microsecond)
    cookie_datetime = epoch + timedelta(microseconds=cookie_microseconds_since_epoch)
    return str(cookie_datetime)

def buildDict(json):
    theDict = {}

    for query in json['event']:
        theDict[microsecondToDateTime(query['query']['id'][0]['timestamp_usec'])] = query['query']['query_text']
    
    return theDict

def findAllSearches():
    fileList = []
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.endswith('.json'):
                fileList.append(os.path.join(root, file))
    
    return fileList

searchableFiles = findAllSearches()
allParsedContents = {}

for jsonFile in searchableFiles:
    allParsedContents.update(buildDict((readFile(jsonFile))))

ordered_dict = OrderedDict(sorted(allParsedContents.items(), key=lambda x: parse(x[0])))

for givenDate,searchQuery in ordered_dict.items():
    print givenDate,searchQuery