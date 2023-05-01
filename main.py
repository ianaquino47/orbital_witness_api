from typing import List
from fastapi import FastAPI, Query
from database import call_database
from title import TitleBasic
from utils import filter_by_title_class, get_paginated_data, get_sort_keys, sort_data

app = FastAPI()

@app.get("/api/titles")
async def get_all_titles(
    title_class: str = Query(None),
    _sort: str = Query(None),
    _order: str = Query('asc'),
    _page: int = Query(1, ge=1),
    _limit: int = Query(None, ge=1, le=100),
) -> List[TitleBasic]:
    try:
        # Mock database call
        titles_data = await call_database()

        # Filter by title_class if specified
        filtered_titles = filter_by_title_class(titles_data, title_class)

        # Parse _sort and _order query parameters
        sort_params = _sort.split(",") if _sort else []
        order_params = _order.split(",") if _order else []

        # Create a list of tuples (key, reverse) to pass to sorted()
        sort_keys = get_sort_keys(sort_params, order_params)

        # Sort the list using multiple keys (default = asc)
        sorted_titles = sort_data(filtered_titles, sort_keys)

        # Apply pagination
        paginated_titles = get_paginated_data(sorted_titles, _page, _limit)
        
        return paginated_titles
    except:
        raise