CREATE TABLE weather_report(
	site_num INT,
	temperature_2m INT,
	wind_gusts_10m INT,
	wind_direction_10m INT,
	date_time TEXT DEFAULT (datetime('now'))
);
