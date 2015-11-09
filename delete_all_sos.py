#!/bin/bash

import sys
import json
import requests

def check_resp(resp):
    if resp.status_code != 204:
        print "Error deleting the SO"
        print 'resp.status_code = ' + str(resp.status_code)
        print 'resp.text = ' + resp.text


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
headers['Authorization'] = 'NDU0NDg1NzktNzkwZS00NGI3LTkyNWQtMDQwMWQ1ODEyM2M3ZGU0N2RlMzEtY2Y1Yy00NDI0LWIxN2QtNGQ1MzRkNzIwMTlm'

# print ids

# import ipdb; ipdb.set_trace() # BREAKPOINT
# # Delete Sensors
# print ids['photocell']
# resp = requests.delete('http://api.servioticy.com/' + ids['photocell'], headers=headers)
# check_resp(resp)
# print ids['tempsensor']
# resp = requests.delete('http://api.servioticy.com/' + ids['tempsensor'], headers=headers)
# check_resp(resp)
# print ids['humiditysensor']
# resp = requests.delete('http://api.servioticy.com/' + ids['humiditysensor'], headers=headers)
# check_resp(resp)

# Delete elements
import ipdb; ipdb.set_trace() # BREAKPOINT
for key, value in ids.iteritems():
    element = key.split('-')[0]
    if element == 'blind':
        headers['Authorization'] = users[key.split('-')[1]]
        resp = requests.delete('http://api.servioticy.com/' + value, headers=headers)
        check_resp(resp)
    elif element == 'aacc':
        headers['Authorization'] = users[key.split('-')[1]]
        resp = requests.delete('http://api.servioticy.com/' + value, headers=headers)
        check_resp(resp)
    elif element == 'photocell':
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



