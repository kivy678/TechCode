# -*- coding:utf-8 -*-

import concurrent.futures
import asyncio


def printf(v):
    print(v)

async def Tesker(values):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                printf,
                val
            ) for val in values
        ]
        #for i in futures:
        #    i.add_done_callback(self.complete_cb)

if __name__ == '__main__':
    Tesker([i for i in range(100)])

    print('main done...')
