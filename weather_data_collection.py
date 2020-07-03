import json
import requests
import csv
import pandas as pd

class Weather:
	def getWeather(self, station):
		URL = "https://api.meteostat.net/v1/history/daily?station={}&start=2016-01-01&end=2019-12-31&key=yhve1Ihj".format(station)
		download = requests.get(url = URL)
		data = download.json()
		weather_d = data['data']
		print(type(weather_d))

		with open('bakersfield_weather_2016_to_2019.csv', 'a+', newline='\n') as outfile:
			f = csv.writer(outfile)
			f.writerow(["date","temperature", "temperature_min", "temperature_max", "precipitation", "snowfall", "snowdepth", "winddirection", "windspeed", "peakgust", "sunshine", "pressure"])
			for w in weather_d:
				f.writerow(w.values())
				#print(w)
		outfile.close()

	def getStation(self):
		URL = "https://api.meteostat.net/v1/stations/search?country='US'&key=yhve1Ihj"
		download = requests.get(url = URL)
		data = download.json()
		station = data['data']
		ls_station = []
		for s in station:
			print(s)
			ls_station.append(s['id'])
		return ls_station

w = Weather()
data = w.getStation()