from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


from .models import GoogleAPI

@api_view(['GET'])
def Search(request,format = None):
    API = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyDpbhY2QMOB1bDMR_c11pqq4D-Xsul3Uxg"
    print(request.query_params)
    if 'query' not in request.query_params.keys():
        return Response("Query is Invalid", status=status.HTTP_400_BAD_REQUEST)
    else :
        query = request.query_params['query']
        response = requests.get(API.format(query))
        geodata = response.json()
        #google = GoogleAPI(query)
        #print(google.search())
        return Response(
            #google.search()
            geodata
        )