from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


# create a list for to generate our buttons
part_of_description = [
    'Temperature',
    'Humidity',
    'Pressure',
    'Wind',
    'Sunrise',
    'Sunset',
    'Length of the day'
]


#create the Callback's object instanc
cb = CallbackData('ikb', 'action')


def ikb_all() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in part_of_description:
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_temperature() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in part_of_description[1:]:
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_humidity() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in (part_of_description[:1] + part_of_description[2:]):
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_pressure() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in (part_of_description[:2] + part_of_description[3:]):
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_wind() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in (part_of_description[:3] + part_of_description[4:]):
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_sunrise() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in (part_of_description[:4] + part_of_description[5:]):
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_sunset() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in (part_of_description[:5] + part_of_description[6:]):
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_length() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    for button in (part_of_description[:6] + part_of_description[7:]):
        ikb.insert(InlineKeyboardButton(
            text=f"{button}",
            callback_data=cb.new(f"{button[:4]}")
        ))
    ikb.add(InlineKeyboardButton(
        text="Full report",
        callback_data=cb.new('full')
    ))
    return ikb


def ikb_back() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(
                                                text="Back",
                                                callback_data=cb.new('back')))

    return ikb
