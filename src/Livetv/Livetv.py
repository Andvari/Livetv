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
out_file = open("ready_streams.log", "wb")

url = "http://livetv.ru"
request = urllib2.urlopen(url)
page = request.read()
page = page[page.find("\xf1\xe5\xe3\xee\xe4\xed\xff") : ]

page = page[ : page.find("/allupcoming/")]
page = page.replace("&ndash;", "-")

get_eventinfo(page)

log = open("livetv1.log", "wb")

for i in live:
    print str(live[i]) + " " + links[live[i]]
    req = urllib2.urlopen(links[live[i]])
    page = req.read()
    
    
    webplayer      = re.compile('http://www8.livetv.ru/webplayer.php(.*?)\">').findall(page)
    for link in webplayer:
        print link
    
    
    webplayer2     = re.compile('http://www8.livetv.ru/webplayer2.php(.*?)\">').findall(page)
    for link in webplayer2:
        print link
        '''
        url = "http://www8.livetv.ru/webplayer2.php" + link
        req = urllib2.urlopen(url)
        page = req.read()
        page = page.upper()
        
        log.write("\n1===")
        log.write(url.encode('utf-8'))
        log.write("====\n")
        page = page[ page.find('BROWSERDETECT.BROWSER'): ]
        page = page[ : page.find('\"></IFRAME')]
        
        url = page[ page.rfind('SRC=') + 12 : ]
        
        if(url.find('WWW') == -1):
            url = "WWW." + url
            
        url = "HTTP://" + url
        
        url = url.lower()
        
        #print url
        
        req  = urllib2.urlopen(url)
        page = req.read()
        
        log.write("\n2===")
        log.write(url.encode('utf-8'))
        log.write("====\n")
        log.write(page.encode('utf-8'))
        '''
    
    '''
    redirects = re.compile('redirects/play.php(.*?)\">').findall(page)
    for link in redirects:
        print link
    '''
    
    '''
    bet365    = re.compile('bet365.com/home/(.*?)\">').findall(page)
    for link in bet365:
        url = "http://www.bet365.com/home/" + link
        req = urllib2.urlopen(url)
        page = req.read()
        log.write(page)
        log.write("\n=======================n")
    '''
        

    '''
    bwin      = re.compile('bwin.com/(.*?)\">').findall(page)
    for link in bwin:
        print link
    '''
        
        
    '''
    j=0
    for link in www8:
        url = "http://www8.livetv.ru/" + link
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
    