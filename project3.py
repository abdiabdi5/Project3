
import urllib.request
with urllib.request.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log') as response:
	html = response.read()
import sys
import re
import operator
from datetime import datetime

#Configurations
REMOTE_URL = 'https://s3.amazonaws.com/tcmg412-fall2016/http_access_log'
LOCAL_FILE = 'http_access_log'

# listing out my variables
i = 0
requests_by_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
requests_by_week = {}
requests_by_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
files = {}
counts = {'requests': 0, '300': 0, '400': 0}

regex = re.compile

#  Need to put if statements













print ('Total Requests:', counts['requests'])
print (' ')
print ('400 status:', counts['300'])
print (' ')
print ('300 status:', counts['400'])
print (' ')
print ('requests by day with 0 being sunday and 6 being saturday')
print (requests_by_day)
print (' ')
print ('requests by week starting in October 1994')
print (requests_by_week)
print (' ')
print ('requests by month:')
print (requests_by_month)
print (' ')
print ('Most-requested file:',)

