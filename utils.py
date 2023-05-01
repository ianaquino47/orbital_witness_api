from typing import List, Union
from title import TitleBasic

VALID_SORT_PARAMETERS = ('id', 'title_number', 'title_class')
VALID_ORDER_PARAMETERS = ('asc', 'desc')


def filter_by_title_class(data: List[TitleBasic], title_class: Union[str, None]) -> List[TitleBasic]:
    if title_class:
        filtered_titles = [
            title for title in data if title.title_class.lower() == title_class.lower()]
    else:
        filtered_titles = data
    return filtered_titles


def get_sort_keys(sort_params: List[str], order_params: List[str]) -> List[tuple]:
    sort_keys = []
    for (sort_param, order_param) in (zip(sort_params, order_params)):
        validate_parameter(sort_param, VALID_SORT_PARAMETERS)
        validate_parameter(order_param, VALID_ORDER_PARAMETERS)
        reverse = order_param.lower() == "desc"
        sort_keys.append((sort_param, reverse))
    return sort_keys


def validate_parameter(param: str, valid_parameters: tuple) -> None:
    if (param not in valid_parameters):
        raise CustomException(
            code=404,
            response=response(
                success=False,
                message=f'Invalid paramater: {param}'
            )
        )


def sort_data(data: List, sort_keys: List[tuple]) -> List[TitleBasic]:
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


def get_paginated_data(data: List[TitleBasic], page: int, limit: int) -> List[TitleBasic]:
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
