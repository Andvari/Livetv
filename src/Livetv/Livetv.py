'''
Created on Oct 8, 2012

@author: nemo
'''

import urllib, urllib2, re

log = open("livetv.log", "wb")

url = "http://livetv.ru"
request = urllib2.urlopen(url)
page = request.read()
page = page[page.find("\xf1\xe5\xe3\xee\xe4\xed\xff") : ]
page = page[ : page.find("/allupcoming/")]
page = page.replace("&dash", "-")

tour = re.compile("alt=\"(.*?)\"src").findall(page)
icon_url = re.compile("src=\"(.*?)\"").findall(page)
desc = re.compile("evdesc\">(.*?)<").findall(page)
link = re.compile("eventinfo(.*?)\"").findall(page)
print link[0]