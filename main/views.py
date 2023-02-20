from django.shortcuts import render

import requests


# 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=28ec40469da2d3a2e2462a07ff5cc09b'
def index(request):
    city = request.GET.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=28ec40469da2d3a2e2462a07ff5cc09b&units=metric'
    response = requests.get(url).json()
    context = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon']
    }
    return render(request, 'index.html', context)
