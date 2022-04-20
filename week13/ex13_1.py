import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

serviceurl = 'http://py4e-data.dr-chuck.net/xml?'


#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
total = 0
while True:
    address = input('Enter url: ')
    if len(address) < 1: break

#    parms = dict()
#    parms['address'] = address
#    if api_key is not False: parms['key'] = api_key
#    url = serviceurl + urllib.parse.urlencode(parms)
#    print('Retrieving', url)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    data2 = data.decode()
    print(data2)
    tree = ET.fromstring(data2)
#    print(tree)
    results = tree.findall('comments/comment/count')
    print(results)

#    for num in results:

#    comment_count = results.find('commentinfo').find('comments').findall('comment').find('count').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text
#    total = total + comment_count
    print('Comments: ', total)
