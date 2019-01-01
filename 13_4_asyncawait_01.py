# エキスパートPythonプログラミング 改訂2版 13章
# 非同期プログラミングその１
# async をつけられた関数はコルーチンを返す

import asyncio


async def async_hello():
    print("Hello, World")

if __name__ == "__main__":
    ret = async_hello()
    print(type(ret))  # 返されるものはコルーチン

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_hello())
