# Predict age based on a name

import requests

BASE_URL="https://api.agify.io/"

name=input("Input your name: ")
request_url= f"{BASE_URL}?name={name}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    name=data['name']
    age=data['age']
    checkLetters=False
    for i in range(len(name)):
        if name[i].upper()<'A' or name[i].upper()>'Z': checkLetters=True

    print("You have to introduce a name...with letters!") if checkLetters==True else print(f"Your name is {name} and you are {age} years old!")
    
else:
    print("An error occurred.")