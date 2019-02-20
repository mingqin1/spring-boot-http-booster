#!/usr/bin/python
import requests
r = requests.get('https://api.github.com/events')
print (r.content)
print "Hello World!"
