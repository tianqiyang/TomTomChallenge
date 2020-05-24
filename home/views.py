import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    context = {
        'list': ['a', 'b'],
    }
    #return render(request, 'default.html', { 'mapbox_access_token': mapbox_access_token })
    template = loader.get_template('default.html')
    cookedAsian = [1,2,3,4]
    cookedFastFood = []
    cookedMexican = []
    rawMeat = []
    rawFish = []
    rawVegetables = []
    return HttpResponse(template.render(context, request))
