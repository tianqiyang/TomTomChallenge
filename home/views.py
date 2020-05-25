import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    # template = loader.get_template('default.html')
    context = {
        "food":
            [{
                "x": -122.41157518699714,
                "y": 37.78861143786813,
                "isCook": "cook",
                "type": "asian",
                "food_name": "Pork Rice",
                "Ingredients": "Fried pork, eggs,tomatoes, onions, brown rice",
                "address": "865 Market St, San Francisco, CA 94103",
                "food_image": "img/pork_rice.jpg",
                "restaurant_logo": "img/Panda_Express_logo.png",
                "other_logos": ["img/1.png", "img/324.png", "img/323.png"],
                "descirption": "<img src=\" static 'img/pork_rice.jpg' %}\""
            }, {
                "x": -122.43563039769336,
                "y": 37.79623397692485,
                "food_name": "Dragon Liver Noodle",
                "Ingredients": "Pig liver, noodle",
                "address": "832 Market St, San Francisco, CA 94103",
                "food_image": "img/pork_rice.jpg",
                "restaurant_logo": "img/Panda_Express_logo.png",
                "other_logos": ["img/1.png", "img/324.png", "img/323.png"],
                "descirption": "dragon Liver Noodle"
            }, {
                "x": -122.45373134831641, 
                "y": 37.780423390391235,
                "isCook": "cook",
                "type": "fast_food",
                "food_name": "Burritos",
                "Ingredients": "bread, meat, cheese",
                "address": "901 Market St, San Francisco, CA 94103",
                "food_image": "img/beef_cheese_burritos.jpeg",
                "restaurant_logo": "img/Panda_Express_logo.png",
                "other_logos": ["img/1.png", "img/23.png", "img/323.png"],
                "descirption": "Burritos"
            }
        ]
    }
    return render(request, 'default.html', context)