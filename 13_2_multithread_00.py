# エキスパートPythonプログラミング 改訂2版 13章の最初のサンプルコード

# python-gmaps · PyPI
# https://pypi.org/project/python-gmaps/

# 【2018年7月16日版】Google Maps の APIキー を取得する – ねんでぶろぐ
# https://nendeb.com/276

import json
import time
from gmaps import Geocoding
from util import PLACES, get_config

api = Geocoding(api_key=get_config()["geocode_api_key"])


def fetch_place(place):
    geocoded = api.geocode(place)[0]
    print(f'{geocoded["formatted_address"]:>60s}, {geocoded["geometry"]["location"]["lat"]:6.2f}, {geocoded["geometry"]["location"]["lng"]:6.2f}')


def main():
    for place in PLACES:
        fetch_place(place)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print(f'time elapsed: {elapsed:.2f}s')
