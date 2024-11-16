import json
import requests
import os
from WunderWeather import weather
from pprint import pprint
import secrets

def pull_data():
    print("pulling data from wunderground")

def test_api():
    # print(secrets.WUNDERGROUND_API_KEY)
    request_url = 'http://api.wunderground.com/api/' + secrets.WUNDERGROUND_API_KEY + '/geolookup/conditions/q/MA/Boston.json'
    response = requests.get(request_url)
    # location = response['location']['city']
    # temp_f = response['current_observation']['temp_f']
    # print('current temperature in %s is: %s' % (location, temp_f))
    print(response)

def main():
    # pull_data()
    test_api()

if __name__ == '__main__':
    main()
