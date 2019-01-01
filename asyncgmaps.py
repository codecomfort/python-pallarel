
import aiohttp
from util import get_config

session = aiohttp.ClientSession()


async def geocode(place):
    params = {
        "sensor": "false",
        "address": place,
        "key": get_config()["geocode_api_key"]
    }

    # https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Berlin&key=〜
    async with session.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params=params

    ) as response:
        result = await response.json()
        return result["results"]
