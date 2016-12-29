import requests

city = raw_input("Enter the name of the  city to check the weather details:")

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=<enter your API key here>"

data=requests.get(url)

read=data.json()

print "City Name  : {}".format(read['name'])
print "Temprature : {}F".format(read['main']['temp'])
print "Humidity   : {}".format(read['main']['humidity'])
print "Pressure   : {}".format(read['main']['pressure'])
print "Wind Speed : {}".format(read['wind']['speed'])
print "Description :{}".format(read['weather'][0]['description'])
