import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# ініціалізуєм логер
logger = logging.getLogger(__name__)


# функція конфігурації і запуска бота
async def main():
    # конфігуріруєм логірування
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # виводимо в консоль інформацію про начало запуска бота
    logger.info('Starting bot')

    # загружаєм конфіг в змінну config
    config: Config = load_config()

    # ініціалізуєм бота і диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # реєструєм роутери в диспетчері
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # пропускаєм зібранні апдейти і запускаєм polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
