import asyncio
import logging
from config import bot, dp
from handlers import commands, echo, fsm_add_lesson


dp.include_router(router=commands.router_commands)
dp.include_router(router=fsm_add_lesson.router_add_lesson)
dp.include_router(router=echo.router_echo)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))

    