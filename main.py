"""
This telegram bot allows you to get a weather report at a given point
in time anywhere in the world.
For the bot to work, you need to get an API key in OpenWeather
and your bot token from BotFather in teleram!
"""

import requests

import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboards as keyb

from config import TOKEN_OPEN_WEATHER, TOKEN_API_TELEGRAM


# create the Bot's object instance and the Dispatcher's object instance
bot = Bot(token=TOKEN_API_TELEGRAM, parse_mode='HTML')
dp = Dispatcher(bot)


# start command handler
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await  bot.send_message(chat_id=message.from_user.id,
                            text="Hi! Write me the name of city, I'll send you a weather report!")


# city message handler
@dp.message_handler()
async def get_weather(message: types.Message):

    # create a state of weather + emoji dict
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Dizzle": "Dizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U00001F328",
        "Mist": "Mist \U00001F32B"
    }


    try:
        # make a get-request in OpenWeather by API
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={TOKEN_OPEN_WEATHER}&units=metric")
        data = r.json()


        # get the city from output answer
        city = data["name"]
        cur_weather = data["main"]["temp"]


        # get the weather discription
        weather_description = data["weather"][0]["main"]

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]

        else:
            wd = "Look out the window, I don't understand what the weather is like there!"

        # get values from weather report
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed_wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        # create a list with all values for our bot and make it global, because we will need it in the next handler
        # this method is not recommended, but i didn't figure out how to do it better
        global arr
        arr = [
            city,
            cur_weather,
            wd, humidity,
            pressure,
            speed_wind,
            sunrise_timestamp,
            sunset_timestamp,
            length_of_the_day
            ]

        await bot.send_message(

            chat_id=message.from_user.id,
            text=f"{datetime.datetime.now().strftime('Date:  %d-%m-%Y  |  Time:  %H:%M')}\n"
                 f"Weather in the city: <b>{city}</b>",
            reply_markup=keyb.ikb_all()
            )

    # catch exceptions
    except:
        await message.reply("\U00002620 Check the name of city! \U00002620")


# callback handler for our inline keyboards
@dp.callback_query_handler(keyb.cb.filter())
async def choice_state(callback: types.CallbackQuery, callback_data: dict):

    cb_data_dict = {
        'Temp': [f"Temperature in the city: <b>{arr[1]} C° {arr[2]}</b>", keyb.ikb_temperature()],
        'Humi': [f"Humidity in the city: <b>{arr[3]}%</b>", keyb.ikb_humidity()],
        'Pres': [f"Pressure in the city: <b>{arr[4]} mmHg</b>", keyb.ikb_pressure()],
        'Wind': [f"Wind in the city: <b>{arr[5]} m/s</b>", keyb.ikb_wind()],
        'Sunr': [f"Sunrise in the city: <b>{arr[6]}</b>", keyb.ikb_sunrise()],
        'Suns': [f"Sunset in the city: <b>{arr[7]}</b>", keyb.ikb_sunset()],
        'Leng': [f"Day length in the city: <b>{arr[8]} h</b>", keyb.ikb_length()]
    }

    cb_d = callback_data["action"]


    if cb_d in cb_data_dict.keys():
        await callback.message.edit_text(

                text=f"{datetime.datetime.now().strftime('Date:  %d-%m-%Y  |  Time:  %H:%M')}\n"
                    f"Weather in the city: <b>{arr[0]}</b>\n\n"
                    f"{cb_data_dict[cb_d][0]}",
                reply_markup=cb_data_dict[cb_d][1]
                )

    elif cb_d == 'full':
        await callback.message.edit_text(

                text=f"{datetime.datetime.now().strftime('Date:  %d-%m-%Y  |  Time:  %H:%M')}\n"
                    f"Weather in the city: <b>{arr[0]}</b>\n\n"
                    f"Temperature: <b>{arr[1]} C° {arr[2]}</b>\n"
                    f"Humidity: <b>{arr[3]}%</b>\n"
                    f"Pressure: <b>{arr[4]} mmHg</b>\n"
                    f"Wind: <b>{arr[5]} m/s</b>\n"
                    f"Sunrise: <b>{arr[6]}</b>\n"
                    f"Sunset: <b>{arr[7]}</b>\n"
                    f"Day length in the city: <b>{arr[8]} h</b>\n\n"
                    "*****  Have a good day!  *****\n"
                    '                         ❤️',
                reply_markup=keyb.ikb_back()
                )

    else:
        await callback.message.edit_text(

                text=f"{datetime.datetime.now().strftime('Date:  %d-%m-%Y  |  Time:  %H:%M')}\n"
                    f"Weather in the city: <b>{arr[0]}</b>",
                reply_markup=keyb.ikb_all()
                )


# directly launch the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
