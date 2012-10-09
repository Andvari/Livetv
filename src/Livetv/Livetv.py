'''
Created on Oct 8, 2012

@author: nemo
'''
'''
import re

line = 'abcdef ghijklmnopqrstuvwxyz'

p = re.compile('a(.*?) .*?m(.*?)z').findall(line)

print p[0].pop()
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

get_streams(page)

for i in live:
    print str(live[i]) + " " + links[live[i]]
    req = urllib2.urlopen(links[live[i]])
    page = req.read()
    
    liveurl = re.compile('http://www8.(.*?)\">').findall(page)
    
    j=0
    for link in liveurl:
        url = "http://www8." + link
        req = urllib2.urlopen(url)
        lpage = req.read()
        
        log = open("livetv" + str(i) + "_" +str(j) + ".log", "wb")
        #log.write(lpage)
        #log.close()
        
        if(lpage.find('embed') != -1):
            preurl = lpage[ : lpage.find('embed')]
            preurl = preurl[ preurl.rfind('http') : ]

            posturl = lpage[ lpage.find('embed') : ]
            posturl = posturl[ : posturl.find('>') - 1]

            url = preurl + posturl
            
            if(url.find('ilive.to') == -1):
                id = lpage [ lpage.find('fid=') + 5 : ]
                id = id[ : id.find('\'')]
                vw = lpage [ lpage.find('v_width=') + 8 : ]
                vw = vw[ : vw.find(';')]
                vh = lpage [ lpage.find('v_height=') + 9 : ]
                vh = vh [ : vh.find(';')]
                url = url.replace('js', 'php')
                url += '?live=' + id + '?vw=' + vw + '?vh=' + vh
                
            print str(i) + " " + str(j) + " " + url
            req = urllib2.urlopen(url)
            page = req.read()
            
            log.write(page)
            log.close()
        j+=1

'''

print page

url = page[page.find("src='") + 5 :]
url = url[: url.find("'")]


req = urllib2.urlopen(url)

page = req.read()

swfUrl = page[ page.find('param name = "movie"') : ]
swfUrl = swfUrl[ swfUrl.find('http') : ]
swfUrl = swfUrl[ : swfUrl.find('swf') + 2]

print swfUrl

log.write(page)
'''

'''
for i in livelinks:
    log.write("http://www8." + str(i))
    log.write("\n")
'''
    