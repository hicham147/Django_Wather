from django.shortcuts import render
import requests
from django.http import  HttpResponseRedirect
import datetime
def index(request):
    
    lang = request.GET.get('lang', 'en')

    if 'city' in request.POST :
        city = request.POST['city']
    else:
        city = "london"
    API_key = '830db4d0f16b97ed1829d99f82dcd031'
    
    url = f'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city,'appid':API_key,'units':'metric','lang':lang}
    response = requests.get(url,params=PARAMS)
    data = response.json()
    if response.status_code == 200:
        context = {
            'day':datetime.date.today(),
            'temperature': data['main']['temp'],
            'description':data['weather'][0]['description'],
            'humidity':data['main']['humidity'],
            'city': city,
            'wind_speed':data['wind']['speed'],
            'icon': data['weather'][0]['icon'],
        }
        return render(request, 'index.html',context)
    else:
        message = "Something went wrong!"
        return HttpResponseRedirect(request.path_info + "?message=" + message)

