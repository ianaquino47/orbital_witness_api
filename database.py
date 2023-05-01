import asyncio
import json


async def call_database(res_time: float = 0.1):
    await asyncio.sleep(res_time)
    with open('data.json', 'r') as data:
        titles_data = json.load(data)
        return titles_data