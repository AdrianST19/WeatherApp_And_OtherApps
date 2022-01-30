from urllib import request
import requests

name = input("Input your name: ")

# Name age
BASE_URL = "https://api.agify.io/"
request_url = f"{BASE_URL}?name={name}"
response = requests.get(request_url)

# Name origin
BASE_URL2 = "https://api.nationalize.io/?name="
request_url2 = f"{BASE_URL2}{name}"
response2 = requests.get(request_url2)

if response.status_code == 200 and response2.status_code == 200:
    # If everything is ok, it prints the age based on the name
    data = response.json()
    name = data['name']
    age = data['age']
    checkLetters = False
    for i in range(len(name)):
        if name[i].upper() < 'A' or name[i].upper() > 'Z':
            checkLetters = True

    print("You have to introduce a name...with letters!") if checkLetters == True else print(
        f"Your name is {name} and you are {age} years old!")

    # If everything is ok, it prints the origin of the name
    data2 = response2.json()
    print(f"The origins of the name {name} are:")
    i = 0
    while i < len(data2['country']):
        print("Country: ", data2['country'][i]['country_id'])
        print("Probability: ", round(
            data2['country'][i]['probability'], 2), "%")
        i += 1
else:
    print("Something went wrong, try again!")
