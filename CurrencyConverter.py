from flask import request
import requests

BASE_URL = "https://open.er-api.com/v6/latest/"
coin = input("Input the first coin: ").upper()
compare = input("Input the coin that you would like to compare with: ").upper()
request_url = f"{BASE_URL}{coin}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(f"One {coin} equals {data['rates'][compare]} {compare}")
else:
    print("Something went wrong!")
