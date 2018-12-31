# エキスパートPythonプログラミング 改訂2版 13章
# マルチプロセスその５
# multiprocessing.dummy でマルチスレッドも可能

from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
from threading import current_thread
import os
from gmaps import Geocoding
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


def fetch_place(place):
    geocoded = api.geocode(place)[0]
    return geocoded, f'process: {os.getpid()}, thread: {current_thread().name}'


def present_result(geocoded, process_name):
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{process_name}]')


PROCESS_POOL_SIZE = 4


def main(use_threads=False):
    if use_threads:
        pool_cls = ThreadPool
    else:
        pool_cls = ProcessPool

    with pool_cls(PROCESS_POOL_SIZE) as pool:
        results = pool.map(fetch_place, PLACES)

        for result in results:
            present_result(*result)


if __name__ == "__main__":
    main(False)  # マルチプロセス、シングルスレッド
    # main(True)    # シングルプロセス、マルチスレッド
