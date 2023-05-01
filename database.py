import asyncio
import json
from typing import List
from title import Title, TitleBasic
from utils import CustomException, response


async def call_database(id: int = None, res_time: float = 0.1):
    await asyncio.sleep(res_time)
    with open('data.json', 'r') as data:
        titles_data = json.load(data)
    if (id or id == 0):
        return find_title_by_id(id=id, data=titles_data)
    else:
        data = [TitleBasic(**title) for title in titles_data]
        return data


def find_title_by_id(id: int, data: List) -> Title:
    # finds the title with matching id
    title = next((Title(**title)
                  for title in data if int(title['id']) == id), None)
    if title:
        return title
    else:
        res = response(
            success=False, message=f'Title with id: {id} not found.')
        raise CustomException(code=404, response=res)
