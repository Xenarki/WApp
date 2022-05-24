from django.shortcuts import render
import requests

# Create your views here.
def index(request):
     appid = 'd7343a5dee996549535fba8d79a88546'
     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

     city = 'London'
     res = requests.get(url.format(city)).json()
     print(res.text)

     return render(request, 'weatherapp/index.html')
