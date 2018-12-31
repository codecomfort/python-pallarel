# エキスパートPythonプログラミング 改訂2版 13章
# マルチプロセスその４
# multiprocessing でプロセスプーリング

from multiprocessing import Pool
import os
from gmaps import Geocoding
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


def fetch_place(place):
    geocoded = api.geocode(place)[0]
    return geocoded, f'process-{os.getpid()}'


def present_result(geocoded, process_name):
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f} [{process_name}]')


PROCESS_POOL_SIZE = 4


def main():
    with Pool(PROCESS_POOL_SIZE) as pool:
        results = pool.map(fetch_place, PLACES)

        for result in results:
            present_result(*result)


if __name__ == "__main__":
    main()
