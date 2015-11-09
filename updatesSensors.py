#!/bin/bash

import sys
import json
import requests
import random
import time
import threading

def check_resp(resp):
    if resp.status_code != 202:
        print "Error updating the SO"
        print 'resp.status_code = ' + str(resp.status_code)
        print 'resp.text = ' + resp.text

def newIlu():
    return round((random.random() * (500 - 250) + 250), 60)

def newTemperature():
    return round((random.random() * (22.99 - 18.00) + 18.00), 2)

def newHumidity():
    return round((random.random() * (70 - 85) + 18.00), 5)


ids = {}
f = json.load(open('ids.txt', 'rb'))
for key, value in f.iteritems():
    ids[key] = value

users = {}
with open("users") as f:
    for line in f:
        users[line.rstrip('\n')] = f.next().rstrip('\n')
        next(f)

headers = {'Content-Type': 'application/json'}

def update():
    import ipdb; ipdb.set_trace() # BREAKPOINT
    # Update elements
    for key, value in ids.iteritems():
        element = key.split('-')[0]
        if element == 'photocell':
            headers['Authorization'] = users[key.split('-')[1]]

            data = {}
            channels = {}
            ilu = {}
            ilu["current-value"] = newIlu()
            channels["illumination"] = ilu
            data["channels"] = channels
            data["lastUpdate"] = long(time.time())

            resp = requests.put('http://api.servioticy.com/' + value + '/streams/status', headers=headers, data=json.dumps(data))
            check_resp(resp)
            print data
        elif element == 'tempsensor':
            headers['Authorization'] = users[key.split('-')[1]]

            data = {}
            channels = {}
            temp = {}
            temp["current-value"] = newTemperature()
            channels["temperature"] = temp
            data["channels"] = channels
            data["lastUpdate"] = long(time.time())

            resp = requests.put('http://api.servioticy.com/' + value + '/streams/status', headers=headers, data=json.dumps(data))
            check_resp(resp)
            print data
        elif element == 'humiditysensor':
            headers['Authorization'] = users[key.split('-')[1]]

            data = {}
            channels = {}
            humidity = {}
            humidity["current-value"] = newHumidity()
            channels["humidity"] = humidity
            data["channels"] = channels
            data["lastUpdate"] = long(time.time())

            resp = requests.put('http://api.servioticy.com/' + value + '/streams/status', headers=headers, data=json.dumps(data))
            check_resp(resp)
            print data

    threading.Timer(5, update).start()

update()
