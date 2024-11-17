from db_connection import *
from openmeteo import *

import schedule
import time

url = 'httpS://api.open-meteo.com/v1/forecast'
# params for what data is being pulled, Long and Lat can be adjusted wihtout any changes 
params = {
    'latitude': [40.01, 52.52, 42.5],
    'longitude': [-105.27, 13.41, -103.00],
    'current': ['temperature_2m', 'wind_direction_10m', 'wind_gusts_10m'],
}

def save_current_data():
    current_reports = get_data(url, params)

    site_0_current = current_reports[0].Current()
    site_1_current = current_reports[1].Current()
    site_2_current = current_reports[2].Current()

    current_data = [
        {'site_num': 0, 'temperature_2m': site_0_current.Variables(0).Value(), 'wind_gusts_10m': site_0_current.Variables(1).Value(), 'wind_direction_10m': site_0_current.Variables(2).Value()},
        {'site_num': 1, 'temperature_2m': site_1_current.Variables(0).Value(), 'wind_gusts_10m': site_1_current.Variables(1).Value(), 'wind_direction_10m': site_1_current.Variables(2).Value()},
        {'site_num': 2, 'temperature_2m': site_2_current.Variables(0).Value(), 'wind_gusts_10m': site_2_current.Variables(1).Value(), 'wind_direction_10m': site_2_current.Variables(2).Value()},
    ]
    insert_dynamic(current_data)
    
def main():
    # create_table()
    # save_current_data()
    # read()
    schedule.every(5).minutes.do(save_current_data)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()


'''
todo:
x1. collect data from multiple locations
x2. save data (postgres, csv, ???)
x3. schedule script (Maybe use python apscheduler?)
'''
