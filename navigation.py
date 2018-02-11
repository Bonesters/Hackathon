from key import key #import my key
import urllib.request
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

def time_dist(origin,destination):
    origin = str(origin).replace(' ','+')
    destination =  str(destination).replace(' ','+')
    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,key)

    request = endpoint + nav_request

    resource = urllib.request.urlopen(request)
    response = resource.read().decode(resource.headers.get_content_charset())
    directions = json.loads(response)

    status = directions['status']
    if(status != 'OK'):
        print("No rout, {}".format(status))
        return ("ERROR","ERROR")

    routs = directions['routes']

    for rout in routs[:10]:
        legs = rout['legs']
        distance = legs[0]['distance']['text']
        duration = legs[0]['duration']['text']
        return (duration,distance)
    