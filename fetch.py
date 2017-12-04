from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json


def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')


query = "tree"
name = query

query= query.split()
query='+'.join(query)

url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

soup = get_soup(url,header)

link = json.loads(soup.a.text)["ou"]  
Type = json.loads(soup.a.text)["ity"]

DIR="Pictures"

if not os.path.exists(DIR):
            os.mkdir(DIR)
        
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)

try:
    req = urllib2.Request(Link, headers={'User-Agent' : header})
    raw_img = urllib2.urlopen(req).read()

    if len(Type)==0:
        f = open(os.path.join(DIR , name + "_"+".jpg"), 'wb')
    else :
        f = open(os.path.join(DIR , name + "_"+"."+Type), 'wb')


    f.write(raw_img)
    f.close()
except Exception as e:
    print "could not load : "+img
    print e
