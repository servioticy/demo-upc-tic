#!/bin/bash

import sys
import json
import requests
import random

def check_resp(resp):
    if resp.status_code != 204:
        print "Error deleting the SO"
        print 'resp.status_code = ' + str(resp.status_code)
        print 'resp.text = ' + resp.text

def newIlu():
    return round((random.random() * (500 - 250) + 250), 60)

def newTemperature():
    return round((random.random() * (22.99 - 18.00) + 18.00), 2)


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

# Update elements
import ipdb; ipdb.set_trace() # BREAKPOINT
for key, value in ids.iteritems():
    element = key.split('-')[0]
    if element == 'photocell':
        headers['Authorization'] = users[key.split('-')[1]]
        resp = requests.delete('http://api.servioticy.com/' + value, headers=headers)
        check_resp(resp)
    elif element == 'tempsensor':
        headers['Authorization'] = users[key.split('-')[1]]
        resp = requests.delete('http://api.servioticy.com/' + value, headers=headers)
        check_resp(resp)
    elif element == 'humiditysensor':
        headers['Authorization'] = users[key.split('-')[1]]
        resp = requests.delete('http://api.servioticy.com/' + value, headers=headers)
        check_resp(resp)
