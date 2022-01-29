import requests

API_KEY = "1522c9a9db873d7c4af5a19a32033d2b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}" #api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    feels_like= round(data["main"]["feels_like"] - 273.15, 2)
    temp_min= round(data["main"]["temp_min"] - 273.15, 2)
    temp_max= round(data["main"]["temp_max"] - 273.15, 2)
    city=data['name']
    country=data['sys']['country']

    print(f"\nCountry: {country} \nName of the city: {city} \nWeather: {weather}")
    print(f"Temperature: {temperature} celsius \nFeels like: {feels_like} celsius")
    print(f"Max temperature: {temp_max} celsius \nMin temperature: {temp_min} celsius")
else:
    print("An error occurred.")