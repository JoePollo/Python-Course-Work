from requests import get as reqGet
from datetime import datetime, timedelta
from time import sleep
import smtplib

lat = 0
long = 0
running = False
email = ""
###APIS####
issAPI = reqGet(url = "http://api.open-notify.org/iss-now.json")
issAPI.raise_for_status()
issCoordinates = {
    "issLong": issAPI.json()["iss_position"]["longitude"],
    "issLat": issAPI.json()["iss_position"]["latitude"]
}
issTime = timedelta(
    hours = datetime.utcfromtimestamp(issAPI.json()["timestamp"]).hour,
    minutes = datetime.utcfromtimestamp(issAPI.json()["timestamp"]).minute,
    seconds = datetime.utcfromtimestamp(issAPI.json()["timestamp"]).second
)
timeOfDay = reqGet(url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}")
timeOfDay.raise_for_status()
unformattedSunrise = datetime.strptime(timeOfDay.json()["results"]["sunrise"], "%I:%M:%S %p")
formattedSunrise = timedelta(hours = unformattedSunrise.hour, minutes = unformattedSunrise.minute,
                             seconds = unformattedSunrise.second)
unformattedSunset = datetime.strptime(timeOfDay.json()["results"]["sunset"], "%I:%M:%S %p")
formattedSunset = timedelta(hours = unformattedSunset.hour, minutes = unformattedSunset.minute,
                             seconds = unformattedSunset.second)
now = timedelta(hours = datetime.strptime(datetime.now().strftime("%I:%M:%S %p"), "%I:%M:%S %p").hour,
                minutes = datetime.strptime(datetime.now().strftime("%I:%M:%S %p"), "%I:%M:%S %p").minute,
                seconds = datetime.strptime(datetime.now().strftime("%I:%M:%S %p"), "%I:%M:%S %p").second)
###FUNCTIONS###
def location_finder():
    return issCoordinates["issLong"] < long+5 or issCoordinates["issLong"] > long-5 and issCoordinates["issLat"] < lat+5 or issCoordinates > lat-5
def time_finder():
    return now >= formattedSunset and now <= formattedSunrise
###RUNTIME###
while location_finder() and time_finder():
    sleep(60)
    with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(user = email, password = "")
        gmail_connection.sendmail(from_addr = email, to_addrs = email, msg = "ISS Alert\n\nLookup for the ISS!")
