import random

from lexicon.lexicon_ru import LEXICON_RU


# функція, яка вертає випадковий вибір бота в грі
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# Функція, що повертає ключ зі словника, за яким
# зберігається значення, що передається як аргумент - вибір користувача
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


# функція, яка повертає переможця
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
