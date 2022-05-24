from django.shortcuts import render
import requests

# Create your views here.
def index(request):
     appid = 'd7343a5dee996549535fba8d79a88546'
     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

     city = 'Barnaul'
     res = requests.get(url.format(city)).json()

     city_info = {
          'city': city,
          'temp': res['main']['temp'],
          'icon': res['weather'][0]['icon']
     }

     context = {'info': city_info}

     return render(request, 'weatherapp/index.html', context)
