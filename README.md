# "Камінь, ножиці, Бумага" game in a Telegram bot
___
__Description of interaction with the bot:__

The user starts communicating with the bot by sending the /start command. The bot welcomes the user and offers to play the game, sending a keyboard with the answers "Давай!" and "Не хочу!", and also offers the user to read the detailed rules, sending the /help command.

At this point, the user can take four actions:
```
1. Agree to play the game with the bot by pressing the normal "Давай!" button.
2. Disagree to play with the bot by pressing the normal "Не хочу!" button.
3. Send a chat command /help.
4. Send any other message to the chat.
```
If the user clicks the normal "Давай!" button, the bot will send a chat message "Чудово! Роби свій вибір!" and sends the chat keyboard with "Камінь, ножиці" and "бумага" selection buttons.

At this point, the user can take 3 actions:
```
1. Press one of the selection buttons ("Stone", "Scissors" or "Paper").
2. Send a chat command /help.
3. Send any other message to the chat.
```
If the user clicks one of the selection buttons, the bot generates a random answer from the same list, checks who won, and informs the user of the result. The bot then sends the user an offer to play again and a choice keyboard with "Давай!" and "Не хочу!" buttons.

If the user clicks the "Не хочу!" button, the keyboard is minimized and the bot sends the message "Шкода...\nЯкщо захочеш зіграти, просто розкрий '
          'клавіатуру і нажми кнопку "Давай!"

If the user sends the chat command /help, the bot sends into the chat the rules of the game, an offer to play and the keyboard with buttons "Давай!" and "Не хочу!

If the user sends any other message to the chat, the bot sends a message to the chat that it does not understand the user.