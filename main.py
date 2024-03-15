#############################################


# MODULES & ART
import art
from art import *
import requests
from bs4 import BeautifulSoup
import lxml
import geopy
from geopy import Nominatim

title = text2art("--iCode--")
print(title, "\n\n\n")


#############################################


# WEBSCRAPING
rpi_url = "https://www.adafruit.com/product/4296"
rpi_webpage = requests.get(rpi_url)

soup = BeautifulSoup(rpi_webpage.content, features="lxml")


try:
		#For Amazon.com
		price = soup.select("#priceblock_ourprice")[0].get_text()
except:
		try:
				#For Adafruit.com
				price = soup.select(".product-price")[0].get_text()
		except:

				price = "nil"


#############################################


# WEATHER
geolocater = Nominatim(user_agent="iCode_WebScraping_FinalProject")
location = geolocater.geocode("Frisco, TX")
weatherURL = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(
		location.latitude) + "&lon=" + str(
				location.longitude
		) + "&units=imperial&appid=35d90d11abcf8c775321a869e5bcaf50"

wresponse = requests.get(weatherURL)
json = wresponse.json()
main = json['main']
temp = main['temp']


#############################################


# FINAL OUTPUT
currentTemp = "- The current temperature is: " + str(temp) + "°F"
priceString = f"- The Raspberry Pi 4 is currently priced at: {price}"
print(priceString, "\n", currentTemp)  


#############################################