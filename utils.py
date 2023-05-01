from typing import List, Union
from title import TitleBasic


def filter_by_title_class(data: List[TitleBasic], title_class: Union[str, None]) -> List:
    if title_class:
        filtered_titles = [
            title for title in data if title.title_class.lower() == title_class.lower()]
    else:
        filtered_titles = data
    return filtered_titles


def get_sort_keys(sort_params: List, order_params: List) -> List:
    sort_keys = []
    for (sort_param, order_param) in (zip(sort_params, order_params)):
        reverse = order_param.lower() == "desc"
        sort_keys.append((sort_param, reverse))
    return sort_keys


def sort_data(data: List, sort_keys: List) -> List:
    sorted_titles = data
    if sort_keys:
        # sorting is stable, hence we can do it in reverse order
        for sort_param, order_param in reversed(sort_keys):
            sorted_titles.sort(
                # id is a string hence we need to parse it for correct sorting
                key=lambda title: int(
                    getattr(title, sort_param)) if sort_param == 'id' else getattr(title, sort_param),
                reverse=order_param
            )

    return sorted_titles


def get_paginated_data(data: List, page: int, limit: int) -> List[TitleBasic]:
    if limit:
        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_titles = data[start_index:end_index]
    else:
        paginated_titles = data
    return paginated_titles

class CustomException(Exception):
    def __init__(self, response: dict, code: int):
        self.response = response
        self.code = code

def response(success: bool = True, message: str = '', data: dict = {}) -> dict:
    res = {'success': success, 'data': data}
    if message:
        res['message'] = message
    return res