# エキスパートPythonプログラミング 改訂2版 13章
# 非同期プログラミングその５
# Executor と Future
# Executor.sumbit は Future を返す
# 同期的なものが非同期的に扱えるようになる

from concurrent.futures import ThreadPoolExecutor
import time


# 同期的なメソッド
def loudy_return():
    print("processing")
    time.sleep(2)
    return 42


with ThreadPoolExecutor(1) as executor:
    # submit は Future を返す
    future = executor.submit(loudy_return)
    # Future は いわば Promise のようなもので、完了を待って値を返してくれる
    print(future.result())
