from django.db import models
from rest_framework import serializers
from .PlaceSerializer import PlaceSerializer
import requests

# Create your models here.
class GoogleAPI():
    def __init__(self,query):
        self.API = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyDpbhY2QMOB1bDMR_c11pqq4D-Xsul3Uxg"
        self.query = self.API.format(query)

    def format(self):
        places = []
        response = requests.get(self.query).json()
        for res in response["results"]:
            id = res["place_id"]
            provider = "Google"
            name = ""
            for add in res["address_components"]:
                if "administrative_area_level_1" in add["types"]:
                    name = add["long_name"]
                    break
            address = res["formatted_address"]
            description = address
            location = [res["geometry"]["location"]["lat"],res["geometry"]["location"]["lng"]]
            place = Place(id,provider,name,description,address)
            places.append(place)
        return places

    def search(self):
        places = self.format()
        placeSerial = [PlaceSerializer(p).data for p in places]
        return placeSerial

class Place(object):
    def __init__(self, ID, Provider, Name, Description, Address):
        self.ID = ID
        self.Provider = Provider
        self.Name = Name
        self.Description = Description
        #self.Location = Location
        self.Address = Address