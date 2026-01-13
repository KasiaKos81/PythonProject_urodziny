# Create a program, which will scheck if it is going to rain on a particular day
#
# Program asks for a weather check in a given place and on given date. Use the below given API. It should work like this:
#
# - program asks for which date the weather shall be checked. Data has to be in format of YYYY-mm-dd, i.e. 2022-07-01.
# - if the date is not provided the app considers the next day as a target date
# - the app will make a call to the API to check the weather
# - there are three options to be received as a response about if it is going to rain:
#  1 - rain
#  2 - no rain
#  3 - no f*** idea
#  - the response should be stored in a file. If the searched date is already present in a file return the response from the file
#
# API URL: https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}
#
# the following parameters need to be replaced in the URL: latitude, longitude and searched_date

import requests
from file_handler_rain import FileHandler
#
from geopy.geocoders import Nominatim
file_handler = FileHandler("data.json")

city = input("Provide the name of a city: ")
searched_date = input("Privide date (YYYY-MM-DD): ")

geolocator = Nominatim(user_agent="some_app")
location = geolocator.geocode(city)

print(location)
latitude = location.latitude
longitude = location.longitude

print(file_handler.check_if_date_exists(city, searched_date))

def get_weather_info(latitude, longitude, searched_date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    response = requests.get(url=url)
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("You have put the wrong data")
        return None

response = get_weather_info(latitude, longitude, searched_date)
weather_result = response.get("daily").get("rain_sum")[0]
# weather_info = "rain" if weather_result > 0 else "no rain"

if weather_result > 0:
    weather_info = "rain"
elif weather_result == 0:
    weather_info = "no rain"
else:
    weather_info = "no f*** idea"

print(weather_result)
file_handler.write_file(city, searched_date, weather_info)






