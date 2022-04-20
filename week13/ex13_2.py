import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

while True:
    address = input('Enter url: ')
    if len(address) < 1: break
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    data2 = data.decode()
    info = json.loads(data2)
    for item in info['comments']:
        total = total + item['count']

print(total)
