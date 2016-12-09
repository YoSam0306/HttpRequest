#!/usr/local/python/bin/python
# Time 2016-12-8 9:12
# Author Yo
import urllib,time
import urllib.request as urllib2
import sys,re
if sys.version_info<(3,0):
    import cookielib
else:
    import http.cookiejar as cookielib
def PostLogin(argv,USERNAME,USERPASSWD):
    SESSION=argv['zbx_sessionid']
    HOSTURL=argv['URL']
    ENTER='Sign in'
    AUTOLOGIN=0
    SID=SESSION[16:]
    FORM_REFRESH=1

    data = {'sid': SID, 'form_refresh': FORM_REFRESH, 'name': USERNAME,
            'password': USERPASSWD,
            'autologin': AUTOLOGIN, 'enter': ENTER}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'Referer': HOSTURL,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': '192.168.208.130',
        'Upgrade-Insecure-Requests': '1',
    }

    postdata=urllib.parse.urlencode(data).encode('utf-8')

    request=urllib2.Request(HOSTURL,postdata,header)
    response=urllib2.urlopen(request)
    html=response.read()
    return html
