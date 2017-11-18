import urllib2
from time import sleep

def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('https://google.com',timeout=1)
            return
        except urllib2.URLError:
            sleep(20)
            pass
