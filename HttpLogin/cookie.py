#!/usr/local/python/bin/python
# Time 2016-12-8 9:12
# Author Yo
import urllib,time
import urllib.request as urllib2
import sys,re
if sys.version_info<(3,0):
    import cookielib
else:

def GetCookie(URL):
    cookie=cookielib.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)
    response=opener.open(URL)
    list={}
    for item in cookie:
        list[item.name]=item.value
    list['URL']=URL
    return list
