import asyncio 
import logging

from config import bot, dp 
from handlers import commands, echo, fsm_add_lesson, fsm_add_product 
from database import db

async def main(): # Инициализация базы данных await db.init_db()

# Регистрация обработчиков
    dp.include_router(router=commands.router_commands)
    dp.include_router(router=fsm_add_lesson.router_add_lesson)
    dp.include_router(router=fsm_add_product.router_add_product)
    dp.include_router(router=echo.router_echo)

    await db.init_db()  # Инициализация базы данных
    await db.get_products_db()

# Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

