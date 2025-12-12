import requests

try:
    apikey="fae1b8ea39a0e9063e0b1f9eb627e314"
    city=input("Enter your city : ")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
    response=requests.get(url)
    print("Status code : ",response.status_code)
    # wheatherdata=response.text
    wheatherdata=response.json()
    print()
    print(wheatherdata)

    print("\nTemperature : ",wheatherdata['main']['temp'])
    print("Humidity : ",wheatherdata['main']['humidity'])
    print("Speed : ",wheatherdata['wind']['speed'])



except Exception as e:
    print("Exception :/n",e)