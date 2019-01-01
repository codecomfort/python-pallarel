# エキスパートPythonプログラミング 改訂2版 13章
# 非同期プログラミングその６
# 13_4_asyncawait_04.py では、同期的な実装である python-gmaps の代替として
# asyncgmaps を作ったが、Executor(ThreadPoolExecutor や ProcessPoolExecutor)を使えば、
# python-gmaps を変更せずに非同期的に扱えるようになる。
# Executor/Future を非同期イベントループと共に使用するには、loop.run_in_executor メソッドを使う。
# run_in_executor の第一引数に Executor(ThreadPoolExecutor や ProcessPoolExecutor) を渡せば良い。
# ただし、None を指定しておけば ThreadPoolExecutor(デフォルトのスレッド数) と解釈されるので、
# 自分で Executor を作成して渡す必要はない(concurrent.futures を import も不要)

import asyncio
# from asyncgmaps import geocode, session
from gmaps import Geocoding
from threading import current_thread
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


async def fetch_place(place):
    # run_in_executor は awaitable を返してくれるので、await が使える
    coroutine = loop.run_in_executor(None, api.geocode, place)
    result = await coroutine
    geocoded = result[0]
    return geocoded, current_thread().name


async def present_result(result):
    ret = await result
    geocoded = ret[0]
    thread_name = ret[1]
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{thread_name}]')


async def main():
    coroutines = [present_result(fetch_place(place)) for place in PLACES]
    await asyncio.wait(coroutines)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
