import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def get_data(url, params):
    return openmeteo.weather_api(url, params=params)

def print_current():
    site_num = 0
    for response in responses:
        print(f'-------------[Site #{site_num}]-------------')
        print(f'Cordinates ({response.Latitude()}°N, {response.Longitude()}°E)')
        # print(f'Elevation {response.Elevation()} m asl')
        # print(f'Timezone {response.Timezone()} {response.TimezoneAbbreviation()}')
        # print(f'Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s')

        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        current_wind_direction_10m = current.Variables(1).Value()
        current_wind_gusts_10m = current.Variables(2).Value()
        
        print(f'Current:')
        print(f'    time {current.Time()}')
        print(f'    temperature_2m {current_temperature_2m}')
        print(f'    wind_direction_10m {current_wind_direction_10m}')
        print(f'    wind_gusts_10m {current_wind_gusts_10m}')

        # hourly = response.Hourly()
        # hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        # hourly_data = {'date': pd.date_range(
        #     start = pd.to_datetime(hourly.Time(), unit = 's', utc = True),
        #     end = pd.to_datetime(hourly.TimeEnd(), unit = 's', utc = True),
        #     freq = pd.Timedelta(seconds = hourly.Interval()),
        #     inclusive = 'left'
        # )}
        # hourly_data['temperature_2m'] = hourly_temperature_2m

        # hourly_dataframe = pd.DataFrame(data = hourly_data)
        # print(hourly_dataframe)
        site_num += 1
