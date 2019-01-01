# エキスパートPythonプログラミング 改訂2版 13章
# 非同期プログラミングその３
# await の使用
import time
import random
import asyncio


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4

        # time.sleep(time_to_sleep)   # ブロッキング発生
        # → 出力をみると、bar が全て終わってから foo が出力されている
        # → pallarel になっていない

        await asyncio.sleep(time_to_sleep)  # ブロッキング解放
        # foo で待ちに入ったら bar が実行されるので、出力は交互になる

        print(f'{name} は {time_to_sleep} 秒待機しました')


async def main():
    await asyncio.wait([waiter("foo"), waiter("bar")])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # time コマンドで実行
    # time python 13_4_asyncawait_03.py
