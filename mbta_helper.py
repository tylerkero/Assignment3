# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPQUEST_API_KEY, MBTA_API_KEY
import urllib.request
import json
import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_json(url,location):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    final = url + "?key="+ MAPQUEST_API_KEY + "&location=" + location
    #Waprint (final)
    with urllib.request.urlopen(final) as f:
        response_text = f.read().decode('utf-8')
        # j = json.loads(response_text) # j is a dictionary
        # print(j) 
        #print(response_text)
        data = json.loads(response_text)
        # print(data)
        # print(type(data))
        #pprint.pprint(data)
        return data







def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    data = get_json(MAPQUEST_BASE_URL,place_name)
    
    return(data['results'][0]['locations'][0]['latLng'])

    


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = "https://api-v3.mbta.com/stops?api_key=" + MBTA_API_KEY+ "&filter%5Blatitude%5D=" + str(latitude) + "&filter%5Blongitude%5D=" + str(longitude) +"%22%20-H%20%22accept:%20application/vnd.api+json"
    #print(url)
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # j = json.loads(response_text) # j is a dictionary
        # print(j) 
        #print(response_text)
        data = json.loads(response_text)
        # print(data)
        # print(type(data))
        #pprint.pprint(data)
        #return data
        #pprint.pprint(data['data'][0]['attributes']['name'])
        if data['data'][0]['attributes']['wheelchair_boarding']==0:
            return (data['data'][0]['attributes']['name']), "Not Wheelchair Accessible"
        else:
            return (data['data'][0]['attributes']['name']),"Wheelchair Accessible"


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    first = get_lat_long(place_name)
    latitude = first['lat']
    longitude = first['lng']
    #print(latitude)
    #print(longitude)
    second = get_nearest_station(latitude,longitude)
    return second


def main():
    """
    You can test all the functions here
    
    """
    location = input("Choose a Location: ")
    #get_json(MAPQUEST_BASE_URL,"Washington,DC")
    #print(get_lat_long("location"))
    #get_nearest_station(42.3601,71.0589)
    print("The nearset stop is "+ str(find_stop_near("Washington,DC")))


if __name__ == '__main__':
    main()
