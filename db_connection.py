import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

db_file = 'weather.db'
schema_file = 'schema.sql'

def test_insert():
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
                            insert into weather_report (report_id, site_num, wind_speed, wind_direction) values
                            (0, 0, 20, 250),
                            (1, 1, 20, 210),
                            (2, 2, 20, 180);
                            ''')
        print('Inserted values into the table!')

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
    test_insert()
    read()

if __name__ == '__main__':
    main()