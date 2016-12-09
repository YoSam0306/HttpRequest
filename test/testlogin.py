#!/usr/local/python/bin/python
# Time 2016-12-9 14:51
# Author Yo

import HttpLogin.login as login
import HttpLogin.cookie as cookie

URL="http://192.168.208.130/index.php"
USERNAME='Admin'
USERPASSWD='zabbix'

print("Cookie 获取")
cookiee=cookie.GetCookie(URL)
print(cookiee)
HTML=login.PostLogin(cookiee,USERNAME,USERPASSWD)
print(HTML)