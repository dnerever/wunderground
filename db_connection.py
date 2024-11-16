import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

db_file = 'weather.db'
schema_file = 'schema.sql'

def test_create_insert():
    if check_db(db_file):
        print('Database already exists. Exiting...')
        return

    with open(schema_file, 'r') as rf:
        schema = rf.read()

    with sqlite3.connect(db_file) as conn:
        print('Created the connection')
        conn.executescript(schema)
        print('Created the table! Now inserting')
        conn.executescript('''
                            insert into weather_report (site_num, temperature_2m, wind_gusts_10m, wind_direction_10m) values
                            (0, 20, 20, 250),
                            (1, 21, 20, 210),
                            (2, 22, 20, 180);
                            ''')
        print('Inserted values into the table!')

    print('Automatically closed the connection')

def insert(new_data):
    # if check_db(db_file):
    #     print('Database already exists. Exiting...')
    #     return

    # with open(schema_file, 'r') as rf:
    #     schema = rf.read()

    with sqlite3.connect(db_file) as conn:
        print('Created the connection')
        # conn.executescript(schema)
        # print('Created the table! Now inserting')
        conn.executescript(f'''
                            insert into weather_report (site_num, temperature_2m, wind_gusts_10m, wind_direction_10m) values
                            (3, -17.5, 20, {new_data});
                            ''')
        print('Inserted value(s) into the table!')

    print('Automatically closed the connection')

def read():
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                        SELECT * FROM weather_report
                       ''')
        for row in cursor.fetchall():
            report_id, site_num, wind_speed, wind_direction = row
            print(f'{report_id} {site_num} {wind_speed} {wind_direction}')

def main():
    # test_create_insert()
    insert(100)
    read()

if __name__ == '__main__':
    main()