#!/usr/local/python/bin/python
# Time 2016-12-9 14:51
# Author Yo
import os,sys
parent_path=os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
import HttpLogin.login as login
import HttpLogin.cookie as cookie
URL="http://192.168.208.130/index.php"
USERNAME='Admin'
USERPASSWD='zabbix'
FLAG=sys.argv[1]
print("Cookie 获取")
cookiee=cookie.GetCookie(URL)
HTML=login.PostLogin(cookiee,USERNAME,USERPASSWD)
if FLAG in HTML.decode():
    print("App Online")
else:
    print("App Offline")