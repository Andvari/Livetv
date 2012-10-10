
import re

tour  = {}
links = {}
names  = {}
live  = {}
time = {}

def get_eventinfo(page):
    lines = re.compile("td width=34.*?alt=(.*?)100%").findall(page)
    i=0
    num_active_streams = 0;
    for line in lines:
        tour[i] = line[1:]
        pos   = tour[i].find('"')
        tour[i] = tour[i][ : pos]
        line = line[pos:]
        pos = line.find("eventinfo")
        line = line[pos-1:]
        pos = line.find('"')
        links[i] = "http://livetv.ru" + line[:pos-1]
        line = line[pos+2:]
        pos = line.find("</a>")
        names[i] = line[:pos]
        line = line[pos+2:]
        pos = line.find('class="live"')
        if(pos != -1):
            live[num_active_streams] = i
            num_active_streams += 1
        pos = line.find("evdesc")
        line = line[pos+8:]
        pos = line.find(" ")
        time[i] = line[:pos]
        i += 1
        
'''        
www8 = {}
redirects = {}
bet365 = {}
bwin = {}

def get_sources(page):
    www8      = re.compile('http://www8.livetv.ru/(.*?)\">').findall(page)
    redirects = re.compile('redirects/play.php(.*?)\">').findall(page)
    bet365    = re.compile('bet365.com/home/(.*?)\">').findall(page)
    bwin      = re.compile('bwin.com/(.*?)\">').findall(page)
'''