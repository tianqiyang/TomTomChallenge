import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

#update data that able to render in html
def fixRender(args):
    for cook_type, food_types in args.items():
        for food_type, foods in food_types.items():
            for i in range(len(foods)):
                description = "<p>from prok rice</p>"
                args[cook_type][food_type][i]['description'] = description

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
            "descirption": "from prok rice"
        }, {
            "x": -122.43563039769336,
            "y": 37.79623397692485,
            "food_name": "Food_2",
            "Ingredients": "Fried pork, eggs,tomatoes, onions, brown rice",
            "address": "865 Market St, San Francisco, CA 94103",
            "food_image": "img/pork_rice.jpg",
            "restaurant_logo": "img/Panda_Express_logo.png",
            "other_logos": ["img/1.png", "img/324.png", "img/323.png"],
            "descirption": "from prok rice2"
        }, {
            "x": -122.45373134831641, 
            "y": 37.780423390391235,
            "isCook": "cook",
            "type": "fast_food",
            "food_name": "Food_3",
            "Ingredients": "Fried pork, eggs,tomatoes, onions, brown rice",
            "address": "865 Market St, San Francisco, CA 94103",
            "food_image": "img/pork_rice.jpg",
            "restaurant_logo": "img/Panda_Express_logo.png",
            "other_logos": ["img/1.png", "img/23.png", "img/323.png"],
            "descirption": "from prok rice3"
        }
    ]
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'default.html', context)