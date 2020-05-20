# -*- coding:utf-8 -*-

##########################################################################################

import asyncio
import concurrent.futures

##########################################################################################


def func1(num):
    print(num)


async def Task(executor: concurrent.futures, num) -> tuple:
    try:
        loop = asyncio.get_event_loop()
        res = await loop.run_in_executor(executor, func1, num)

    except Exception as e:
        print(e)


async def Tasker(num):
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = list(
                map(lambda x: asyncio.create_task(Task(executor, x)), num))

            await asyncio.gather(*futures)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    num = list(range(50))
    asyncio.run(Tasker(num))
