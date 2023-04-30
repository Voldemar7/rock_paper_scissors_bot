from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Створимо клавіатуру через ReplyKeyboardBuilder -------

# створимо кнопки з відповідями погодження і відказу
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# ініціалізуєм білдер для клавіатури з кнопками "Давай" і "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# добавляєм кнопки в білдер з параметром width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# створимо клавіатуру з кнопками "Давай" і "Не хочу!"
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)

# ------- Створюєм игрову клавіатуру без використання білдера -------

# створюєм кнопки ігрової клавіатури
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Створюєм игрову клавіатуру з кнопками "Камінь 🗿",
# "Ножиці ✂" и "Бумага 📜" як список списків
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1],
                                                             [button_2],
                                                             [button_3]],
                                                   resize_keyboard=True)
