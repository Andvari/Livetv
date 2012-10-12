'''
Created on Oct 12, 2012

@author: nemo
'''

import urllib2

def stream_letontv(url):
    req = urllib2.urlopen(url)
    
    log = open("rtmp.sh", "wb")
    
    log.write('#!/bin/sh\n')
    log.write("rtmpdump")
    page = req.read()
    
    page = page[ page.find("BrowserDetect.browser") : ]
    page = page[ : page.find('"></IFRAME')]
    
    url2 = page[ page.find('SRC="') + 5 : ]
    
    print url2
    
    req = urllib2.urlopen(url2)
    
    page = req.read()
    
    print page
    
    swfUrl = page[ page.find('new SWFObject("') + 15 : ]
    swfUrl = swfUrl[ : swfUrl.find('.swf') + 4]
    
    file = page[ page.find("so.addVariable('file'") + 23 : ]
    file = file[ : file.find("'")]
    
    tcUrl = page[ page.find("so.addVariable('streamer'") + 27 : ]
    tcUrl = tcUrl[ : tcUrl.find("'")]
    
    pageUrl = "http://leton.tv"
    
    app   = tcUrl[ tcUrl.rfind('/') + 1 : ]
    
    flashVer = '"LNX 11,2,202,238"'
    
    out = "out.flv"
    
    print "swfUrl:   " + swfUrl 
    print "tcUrl:    " + tcUrl
    print "app:      " + app
    print "flashVer: " + flashVer 
    print "file:     " + file 
    print "out:      " + out 
    
    
    log.write(' -r ' + tcUrl)
    log.write(' -a ' + app)
    log.write(' -f ' + flashVer)
    log.write(' -W ' + swfUrl)
    log.write(' -p ' + pageUrl)
    log.write(' -y ' + file)
    log.write(' -o ' + out)
    log.write(' --live --verbose\n')
    
    log.close()
    while(1):
        pass