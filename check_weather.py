import requests

import datetime

from pprint import pprint

from config import TOKEN_OPEN_WEATHER


# we need make a get-request to openweater for getting weather now

# create a function with two arg: city and token
def get_weather(city, TOKEN_OPEN_WEATHER):

    # create a state of weather + emoji dict
    code_to_smile = {
        "Clear": "Clear(Ясно) \U00002600",
        "Clouds": "Clouds(Облачно) \U00002601",
        "Rain": "Rain(Дождь) \U00002614",
        "Dizzle": "Dizzle(Дождь) \U00002614",
        "Thunderstorm": "Thunderstorm(Гроза) \U000026A1",
        "Snow": "Snow(Снег) \U00001F328",
        "Mist": "Mist(Туман) \U00001F32B"
    }

    try:
        # make a get-request in OpenWeather by API
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN_OPEN_WEATHER}&units=metric")
        data = r.json()
        pprint(data)


        # get the city from output answer
        city = data["name"]
        cur_weather = data["main"]["temp"]

        # get the weather discription
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look out the window, I don't understand what the weather is like there!\n(Посмотри в окно, не пойму что там за погода!"


        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed_wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(
        f"***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n"
        f"Weather in the city(Погода в городе): {city}\nTemperature(Температура): {cur_weather}C° {wd}\n"
        f"Humidity(Влажность): {humidity}%\nPressure(Давление): {pressure} mm\nWind(Ветер): {speed_wind} m/s\n"
        f"Sunrise(Восход): {sunrise_timestamp}\nSunset(Закат): {sunset_timestamp}\nLength of the day(Длина солнечного лня): {length_of_the_day}h\n"
        f"Have a good day! (Хорошего дня!)")

    except Exception as ex:
        print(ex)
        print("Check the name of city!")


# request input a city from user
def main():
    city = input("Enter the city: ")
    # call our function
    get_weather(city, TOKEN_OPEN_WEATHER)


if __name__ == '__main__':
    main()
