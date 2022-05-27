import asyncio
import requests

async def getSunriseAndSunsetByCoordinates(latitude, longitude):
    res = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}")
    return res.text

async def main():
    print("redesigned-rotary-phone")
    print("starting data fetch")
    maxLatitude = 90
    minLatitude = -90
    maxLongitude = 90
    minLongitude = -90
    for lat in range(minLatitude, maxLatitude, 0.1):
        for lon in range(minLongitude, maxLongitude, 0.1):
            # todo: invoke functions in async manner
            asyncio.run(getSunriseAndSunsetByCoordinates(lat, lon))

    # todo: await all functions

    # todo: gather data in a structured manner
    
    # todo: display all the data

if __name__ == "__main__" : 
    asyncio.run(main())