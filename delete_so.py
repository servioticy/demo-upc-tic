#!/bin/bash

import sys
import json
import requests

so = sys.argv[1]

print so

headers = {'Content-Type': 'application/json'}
headers['Authorization'] = 'NDU0NDg1NzktNzkwZS00NGI3LTkyNWQtMDQwMWQ1ODEyM2M3ZGU0N2RlMzEtY2Y1Yy00NDI0LWIxN2QtNGQ1MzRkNzIwMTlm'
resp = requests.delete('http://api.servioticy.com/' + so, headers=headers)

if resp.status_code != 204:
    print "Error deleting the SO"
    print 'resp.status_code = ' + str(resp.status_code)
    print 'resp.text = ' + resp.text

# print resp.text
# print resp.status_code
# print resp.headers

