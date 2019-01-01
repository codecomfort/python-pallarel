# エキスパートPythonプログラミング 改訂2版 13章
# 非同期プログラミングその２
# 非同期で複数の処理

import asyncio


async def print_number(number):
    print(number)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print_coroutines = [print_number(number) for number in range(10)]
    wait_coroutine = asyncio.wait(print_coroutines)
    print(type(wait_coroutine))
    loop.run_until_complete(wait_coroutine)
    loop.close()
