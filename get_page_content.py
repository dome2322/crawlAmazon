#coding=utf-8
#!/usr/bin/python

import cookielib
import urllib2,urllib,os

def getPageContent(url):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('Host',"amazon.com"),('User-agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'),('Connection','Keep-Alive'),] 
    result = opener.open(url).read()
    return result
