#!/bin/bash

import json
import requests

users = {}
with open("users") as f:
    for line in f:
        users[line.rstrip('\n')] = f.next().rstrip('\n')
        next(f)

headers = {'Content-Type': 'application/json'}
headers['Authorization'] = 'NDU0NDg1NzktNzkwZS00NGI3LTkyNWQtMDQwMWQ1ODEyM2M3ZGU0N2RlMzEtY2Y1Yy00NDI0LWIxN2QtNGQ1MzRkNzIwMTlm'
# users.itervalues().next()
print headers

ids = {}

# # Deploy photocell
# f = json.load(open('photocell/photocell01.json', 'rb'))
# resp = requests.post('http://api.servioticy.com', headers=headers, data=json.dumps(f))
# ids['photocell'] = resp.json()['id']

# # Deploy humiditysensor
# f = json.load(open('humiditysensor/humiditysensor01.json', 'rb'))
# resp = requests.post('http://api.servioticy.com', headers=headers, data=json.dumps(f))
# ids['humiditysensor'] = resp.json()['id']

# # Deploy tempsensor
# f = json.load(open('tempsensor/tempsensor01.json', 'rb'))
# resp = requests.post('http://api.servioticy.com', headers=headers, data=json.dumps(f))
# ids['tempsensor'] = resp.json()['id']

# Deploy all blinds
import ipdb; ipdb.set_trace() # BREAKPOINT
f = json.load(open('blind/blind01.json', 'rb'))
for key, value in users.iteritems():
    headers['Authorization'] = value
    resp = requests.post('http://api.servioticy.com', headers=headers, data=json.dumps(f))
    ids['blind-'+key] = resp.json()['id']

# Deploy all aaccs
import ipdb; ipdb.set_trace() # BREAKPOINT
f = json.load(open('aacc/aacc.json', 'rb'))
for key, value in users.iteritems():
    headers['Authorization'] = value
    resp = requests.post('http://api.servioticy.com', headers=headers, data=json.dumps(f))
    ids['aacc-'+key] = resp.json()['id']


print ids

f = open('ids.txt', 'w')
f.write(json.dumps(ids))


# print resp.text
# print resp.status_code
# print resp.headers
# resp.text, resp.status_code, resp.headers.items()
