"""
Get weather with location, ip address, lat+long

pincode = 560029
lat_long = '12.91,74.85'
city = 'Bangalore'
url = 'https://www.metaweather.com/api/location/search/?query={}'.format(city)

"""
import json
from pprint import pprint
from urllib.request import urlopen


url = 'https://www.metaweather.com/api/location/2295420'

response = urlopen(url)
data = response.read().decode().strip()
data = json.loads(data)
weather = {
    'City': data['title'],
    'Location': data['parent']['latt_long'],
    'Weather': data['consolidated_weather'][0],
}
# pprint(data)
pprint(weather)
