# エキスパートPythonプログラミング 改訂2版 13章
# マルチスレッドその２
# スレッド数限定版

import time
from gmaps import Geocoding
from threading import Thread, current_thread
from queue import Queue, Empty
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


def fetch_place(place):
    geocoded = api.geocode(place)[0]
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{current_thread().name}]')


def worker(work_queue):
    # 各々のスレッドは、work_queue から取り出して処理する
    # どの都市をどのスレッドが処理するかは、その時次第
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            fetch_place(item)
            work_queue.task_done()


THREAD_POOL_SIZE = 4


def main():
    # Queue はスレッド間の通信用に設計された FIFO
    # (なのでスレッドセーフにデータのやり取りができる)
    work_queue = Queue()
    for place in PLACES:
        work_queue.put(place)

    threads = [
        Thread(target=worker, args=(work_queue,), name=f'thread-{str(ii).zfill(2)}') for ii in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print(f'time elapsed: {elapsed:.2f}s')
    # Thread を 4 本に制限したぶん、多少遅くなる
