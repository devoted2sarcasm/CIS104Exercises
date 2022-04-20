import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

serviceurl = 'http://py4e-data.dr-chuck.net/xml?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter url: ')
    if len(address) < 1: break

    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    results = tree.findall('comments/comment/count')
    counts = tree.findall('.//count')
    total = 0
    for count in counts:
        total = total + int(count.text)

    print('Comments: ', total)
