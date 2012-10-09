'''
Created on Oct 8, 2012

@author: nemo
'''

import urllib, urllib2, re
from get_streams import *

log = open("livetv.log", "wb")

url = "http://livetv.ru"
request = urllib2.urlopen(url)
page = request.read()
page = page[page.find("\xf1\xe5\xe3\xee\xe4\xed\xff") : ]

page = page[ : page.find("/allupcoming/")]
page = page.replace("&ndash;", "-")

log.write(page.encode('utf-8'))

get_streams(page)

for i in links:
    print links[i]