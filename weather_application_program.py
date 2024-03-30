"""
Program Details:

Weather Application

Requirements:
Create a Python Application which asks the user for their zip code or city (Your program must perform both a city and a zip lookup). You must ask the user which they want to perform with each iteration of the program.
Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this is not readable to the average person.  You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
Use comments within the application where appropriate in order to document what the program is doing. Comments should add value to the program and describe important elements of the program.
Use functions including a main function and a properly defined call to main. You should have multiple functions.
Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
Validate whether the user entered valid data. If valid data isn’t presented notify the user. Your program should never crash with bad user input.
Use the Request's library in order to request data from the webservice.
Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
Use Python 3
Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.

Author: Siddhartha Bhaumik
Initial Release Date: 03/02/2022
"""

import requests
import json
import time

print('''Welcome to Weather Channel!!!\nAccess Current Weather Data for any US cities!!\n''')


def main():
    """Main function takes the user input as zip code or city/country name to receive current weather information"""

    api_url = 'https://api.openweathermap.org/data/2.5/weather'

    while True:
        try:
            location = input('\nPlease enter the Zip Code or City name: ')
            # checking if location entered is a valid digit and of length greater than or equal to 5. Also, if its characters
            if (location.isdigit() and (len(location) >= 5)) or location.isalpha() is True:
                current_weather(location, api_url)
                print('----------------')
                new_weather()
                break
            else:
                print('\nPlease enter a valid Zip code or City Name!!!!!\n')
        except KeyError:
            print('-------------------')
            new_weather()
            break


def current_weather(location, api_url):
    """GET request call function to Openweathermap URL"""

    api_token = 'e0658f792164bea0f30488a83ec7f9c9'
    # checking if location entered is a valid digit and of length greater than or equal to 5
    if (location.isdigit() and (len(location) >= 5)) is True:
        params = {'zip': location, 'appid': api_token}
    else:
        params = {'q': location, 'appid': api_token}

    while True:
        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                print('Connection successful...')
                weather_json = json.loads(response.text)
                weather_parsed(weather_json)
                break
            elif response.status_code == 404:
                print('The Zip code or City entered is invalid or not found')
                break
            else:
                print('Something went wrong.Please try again!!')
                break
        except requests.exceptions.ConnectionError as err:
            print('Looks like no internet connection! Please try again later!!!')
            break


def new_weather():
    """Function to check if User wants to check weather for another location"""

    while True:
        try:
            user_input = str(input('Would you like to check weather for another location, Yes or No? ')).upper().strip()
            if user_input == 'YES':
                main()
                break
            elif user_input == 'NO':
                print('Thank you! Please visit again!!')
                break
            else:
                print('\nPlease enter a valid option, Yes or No!!!\n')
        except ValueError:
            continue


def convert_main_temp(main_temp):
    """Converts main temperature from Kelvin to Fahrenheit and Celsius"""
    main_temp_f = round((((main_temp - 273.15) * 9) / 5) + 32)
    main_temp_c = round(main_temp - 273.15)
    return f'{main_temp_f}{chr(176)}F / {main_temp_c}{chr(176)}C'


def convert_high_temp(max_temp):
    """Converts high temperature from Kelvin to Fahrenheit and Celsius"""
    high_temp_f = round((((max_temp - 273.15) * 9) / 5) + 32)
    high_temp_c = round(max_temp - 273.15)
    return f'{high_temp_f}{chr(176)}F / {high_temp_c}{chr(176)}C'


def convert_low_temp(min_temp):
    """Converts low temperature from Kelvin to Fahrenheit and Celsius"""
    low_temp_f = round((((min_temp - 273.15) * 9) / 5) + 32)
    low_temp_c = round(min_temp - 273.15)
    return f'{low_temp_f}{chr(176)}F / {low_temp_c}{chr(176)}C'


def weather_parsed(parsed):
    """Parse Json data for required display columns, Display readable output for end users"""
    city = str(json.dumps(parsed['name']))
    country = str(json.dumps(parsed['sys']['country']))
    timezone = int(json.dumps(parsed['timezone']))
    epoch_time = int(json.dumps(parsed['dt']))
    actual_time = epoch_time + timezone
    curr_time = time.strftime("%A, %b %d, %Y %I:%M %p", time.gmtime(actual_time))
    main_temp = float(json.dumps(parsed['main']['temp']))
    min_temp = float(json.dumps(parsed['main']['temp_min']))
    max_temp = float(json.dumps(parsed['main']['temp_max']))
    curr_pressure = float(json.dumps(parsed['main']['pressure']))
    curr_humidity = float(json.dumps(parsed['main']['humidity']))
    cloud_cover = str(json.dumps(parsed['weather'][0]['description'])).replace('"', '')
    print(f'Weather Report for {city}, {country} on {curr_time}:\n'
          f'Current Temperature: {convert_main_temp(main_temp)}\n'
          f'Current High Temp: {convert_high_temp(max_temp)}\n'
          f'Current Low Temp: {convert_low_temp(min_temp)}\n'
          f'Current Pressure: {curr_pressure} hPa\n'
          f'Current Humidity: {curr_humidity} %\n'
          f'Current Cloud Cover: {cloud_cover}\n')


if __name__ == "__main__":
    main()
