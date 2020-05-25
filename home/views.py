import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def getAllData():
    # return a dictionary of all information that contains restruant and food
    # and import from database
    pass 

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    template = loader.get_template('default.html')
    args = {}
    #args = getAllData()
    #fake data
    args['cook'] = {
        'asian': [
            {
                "coordinates": [-122.41157518699714, 37.78861143786813],
                "description": "restaurant 1"
            }, {
                "coordinates": [-122.43563039769336, 37.79623397692485],
                "description": "restaurant 2"
            }, {
                "coordinates": [-122.45373134831641, 37.780423390391235],
                "description": "restaurant 3"
            }]
    }
    return HttpResponse(template.render(args, request))
