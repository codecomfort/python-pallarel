# エキスパートPythonプログラミング 改訂2版 13章
# マルチスレッドその２
# スロットリングの導入(あとで throttle.py を実装後、組み込む)

import time
from gmaps import Geocoding
from threading import Thread, current_thread
from queue import Queue, Empty
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


def fetch_place(place):
    geocoded = api.geocode(place)[0]
    return geocoded, current_thread().name


def present_result(geocoded, thread_name):
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{thread_name}]')


def worker(work_queue, results_queue):
    # 各々のスレッドは、work_queue から取り出して処理する
    # どの都市をどのスレッドが処理するかは、その時次第
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            try:
                result = fetch_place(item)
            except Exception as err:
                # 例外も結果として返す
                results_queue.put((err, current_thread().name))
            else:
                results_queue.put(result)
            finally:
                work_queue.task_done()


# google の制限が緩和されたのか、サンプルコードの 10 程度では
# 使用制限の例外が出ないので、この程度にして行う
# 何度もやってロックされないよう注意
THREAD_POOL_SIZE = 100


def main():
    # Queue はスレッド間の通信用に設計された FIFO
    # (なのでスレッドセーフにデータのやり取りができる)
    work_queue = Queue()
    results_queue = Queue()

    for place in PLACES * 100:
        work_queue.put(place)

    threads = [
        Thread(target=worker, args=(work_queue, results_queue), name=f'thread-{str(ii).zfill(2)}') for ii in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result[0], Exception):
            raise result[0]
        present_result(*result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print(f'time elapsed: {elapsed:.2f}s')
    # Thread を 4 本に制限したぶん、多少遅くなる
