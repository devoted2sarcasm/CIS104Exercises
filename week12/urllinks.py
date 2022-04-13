# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
repeat = input('Enter count: ')
intrep = int(repeat)
pos = input('Enter position: ')
intpos = int(pos)
count = 0


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

while count <= intrep :
    print(url)
    urllst = list()
    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        urllst.append(newurl)
    #print(urllst[intpos-1])
    url = urllst[intpos-1]
    count += 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
