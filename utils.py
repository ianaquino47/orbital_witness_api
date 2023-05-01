from typing import List, Union
from title import TitleBasic


def filter_by_title_class(data: List[TitleBasic], title_class: Union[str, None]) -> List:
    if title_class:
        filtered_titles = [
            title for title in data if title.title_class.lower() == title_class.lower()]
    else:
        filtered_titles = data
    return filtered_titles