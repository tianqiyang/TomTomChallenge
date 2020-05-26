import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import json
import os

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    # template = loader.get_template('default.html')
    module_dir = os.path.dirname(__file__)
    print(module_dir)
    with open(module_dir + '/data.json', 'r') as f:
        context = json.load(f)
        return render(request, 'default.html', context)