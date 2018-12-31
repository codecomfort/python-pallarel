# エキスパートPythonプログラミング 改訂2版 13章の最初のサンプルコード
# マルチスレッドその１
# 全部スレッド化

import time
from gmaps import Geocoding
from threading import Thread, current_thread
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


def fetch_place(place):
    geocoded = api.geocode(place)[0]
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{current_thread().name}]')


def main():
    threads = []
    for ii, place in enumerate(PLACES):
        thread = Thread(target=fetch_place, args=[
                        place], name=f'thread-{str(ii).zfill(2)}')
        thread.start()
        threads.append(thread)

    while threads:
        threads.pop().join()
        # join() して待たないとすぐに main() を抜けてしまい
        # time elapsed の出力が最初になってしまう


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print(f'time elapsed: {elapsed:.2f}s')
    # 全都市パラレルにやるので、かなり早くなる
