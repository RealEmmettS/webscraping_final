import art
from art import *
import requests
from bs4 import BeautifulSoup
import lxml
import geopy
from geopy import Nominatim

head = text2art("--iCode--")
des = text2art("Zenscrape")
print(head, "\n", des, "\n\n\n")

##########################

# Sign-up for FREE Zenscape account at:
# https://app.zenscrape.com/register?plan=free
headers = {"apikey": "1dd7e4e0-1d7e-11eb-a3bc-8783028280fa"}

params = ((
		"url",
		"https://www.adafruit.com/product/4296"
), )

response = requests.get('https://app.zenscrape.com/api/v1/get',
												headers=headers,
												params=params)
#print(response.text)

#######################

soup = BeautifulSoup(response.content, features="lxml")


try:
		#For Amazon.com
		price = soup.select("#priceblock_ourprice")[0].get_text()
except:
		try:
				#For Adafruit.com
				price = soup.select(".product-price")[0].get_text()
		except:
				price = "nil"


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



currentTemp = "The current temperature is: " + str(temp) + "°F"
priceString = f"The Raspberry Pi 4 is currently priced at: {price}"
print(priceString, "\n", currentTemp)
