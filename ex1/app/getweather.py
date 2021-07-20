import json
import os
import sys
import requests

#This line is entered so that the code below if will only run if this program was not initiated by another python code
if __name__ == "__main__":
    #Collecting the API key environment variable and storing it into python variable CHAVE_API
    CHAVE_API = os.getenv("OWM_API_KEY")
    #Collecting the city name environment variable and storing it into python variable NOME_CIDADE
    NOME_CIDADE = os.getenv("OWM_CITY")
    #Defining that the parameters specified in the API documentation are the same values stored in the python variables above
    parametros_da_API = {
        "q": NOME_CIDADE,
        "appid": CHAVE_API,
        #Converting units to the metric system for easier understanding of information gathered
        "units": "metric"
    }
    #App will display an error message if no city name is specified
    if not NOME_CIDADE:

        print("No city has been specified.")

        sys.exit(1)
    #App will display an error message if no API key is specified
    if not CHAVE_API:

        print("API key not found.")

        sys.exit(1)
    #This variable stores the text resulting of a successful communication with the OpenWeatherMap API
    resposta = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parametros_da_API)
    #The expected outcome will only be displayed if the HTTP request status code is 200 (successful)
    if resposta.status_code == 200:
        
        citynametest = resposta.json().get("name")
        citydescriptiontest = resposta.json().get("weather")[0].get("description")
        citytemperaturetest = resposta.json().get("main").get("temp")
        cityhumiditytest = resposta.json().get("main").get("humidity")

        print("Current weather data (source: https://openweathermap.org/)\nCity: {};\nDescription: {};\nTemperature: {}ºC;\nHumidity: {}%;".format(citynametest, citydescriptiontest, citytemperaturetest, cityhumiditytest))
    #Should there be anything wrong with the variables (invalid city name or API key) the app will display the message below
    else:

        print("Request could not be fulfilled, please review parameters and try again")
