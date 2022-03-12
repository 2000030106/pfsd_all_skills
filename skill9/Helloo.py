import requests,json
url="https://api.openweathermap.org/data/2.5/weather?"
city=input('Enter Your City Name : ')
zip_code=input('Enter your Zip Code : ')
api_key="a9849b62a1b3a1eb78cf828d0a744a20"
new=url+"zip="+zip_code+",us&appid="+api_key
response=requests.get(new)
if(response.status_code==200):
   data=response.json()
   main=data['main']
   temperature = main['temp']
   humadity=main['humidity']
   pressure = main['pressure']
   report=data['weather']
   long=data['coord']
   sun=data['sys']
   wind=data['wind']
   print(f'City : {city}')
   print(f'Zip Code : {zip_code}')
   print(f"Temperature : {temperature}")
   print(f'Humidity : {humadity}')
   print(f"Pressure : {pressure}")
else:
   print("Error in the HTTP request")
#Alaska