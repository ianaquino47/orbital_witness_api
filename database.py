import asyncio
import json

from title import TitleBasic


async def call_database(res_time: float = 0.1):
    await asyncio.sleep(res_time)
    with open('data.json', 'r') as data:
        titles_data = json.load(data)
        data = [TitleBasic(**title) for title in titles_data]
        return data