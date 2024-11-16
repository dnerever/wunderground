import json
import requests
import os
from pprint import pprint

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = 'httpS://api.open-meteo.com/v1/forecast'
params = {
    'latitude': 52.52,
    'longitude': 13.41,
    'hourly': 'temperature_2m'
}
responses = openmeteo.weather_api(url, params=params)

reponse = responses[0]
# print(f'Cordinates {response.Latitude()} *N {response.Longitutde()} E')
# print(f'Elevation {response.Elevation()} m asl')
# print(f'Timezone {response.Timezone()} {response.TimezoneAbbreviation()}')
# print(f'Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s')

hourly = responses[0].Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {'date': pd.date_range(
    start = pd.to_datetime(hourly.Time(), unit = 's', utc = True),
    end = pd.to_datetime(hourly.TimeEnd(), unit = 's', utc = True),
    freq = pd.Timedelta(seconds = hourly.Interval()),
    inclusive = 'left'
)}
hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
