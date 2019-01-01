# エキスパートPythonプログラミング 改訂2版 13章
# 非同期プログラミングその４
#

import asyncio
from asyncgmaps import geocode, session
from threading import current_thread
from util import PLACES, get_config


async def fetch_place(place):
    geocoded = (await geocode(place))[0]
    return geocoded, current_thread().name


async def present_result(geocoded, thread_name):
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{thread_name}]')


async def main():
    # present_result のシグニチャを変更しない場合、
    # コルーチン作成時にいちいち await するので遅い
    coroutines = [present_result(*(await fetch_place(place))) for place in PLACES]
    # coroutines = []
    # for place in PLACES:
    #     fetch_place_result = await fetch_place(place)
    #     present_result_coroutine = present_result(*fetch_place_result)
    #     coroutines.append(present_result_coroutine)

    await asyncio.wait(coroutines)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_until_complete(session.close())
    loop.close()
