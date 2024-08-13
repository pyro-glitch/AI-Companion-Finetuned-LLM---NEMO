""" Search The Web """
import webbrowser as wb

""" Open Apps """
import AppOpener

""" Time Function """
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import time
import requests

class CommandHandler:

    """ Search The Web """
    defaultBrowserName = 'bing'

    def search(self, query):
        query.replace('_', '+')
        wb.get('windows-default').open('https://www.' + self.defaultBrowserName + '.com/search?q=' + query)

    # search("happy_birthday")

    """ Open Apps """
    def openApp(self, name):
        try:
            AppOpener.open(name,output=False, match_closest=True, throw_error=True)
            return "Opening " + name
        except:
            return "I could not find any app with the name " + name

    # print(openApp("recycle"))
    # print(AppOpener.give_appnames())

    """ Time Function """
    def timeOf(self, location_name):
        # find latitude and longitude of region
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(location_name)

        # find timezone by latitude and longitude
        obj = TimezoneFinder()
        timezone = obj.timezone_at(lng=location.longitude, lat=location.latitude)


        # get time through api
        # api-endpoint
        URL = 'https://www.timeapi.io/api/Time/current/zone?timeZone='

        # sending get request and saving the response as response object
        r = requests.get(url=URL + timezone)
        return (r.json()['time'])

    def getTime(self, str):
        if(str == "now"):
            curr_time = time.strftime("%H:%M", time.localtime())
            return "It's " + curr_time + " right now"
        else:
            try:
                return "The current time in {0} is {1}".format(str, self.timeOf(self, location_name=str))
            except:
                return "I guess a issue occurred, maybe network issue :( "

    # getTime("India")

    """ Play Music"""
    def playMusic(self, name):
        # TODO
        return "playing song: "+ name



