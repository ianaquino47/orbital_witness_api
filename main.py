from typing import List, Union
from fastapi import FastAPI, Path, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from database import call_database
from title import Title, TitleBasic
from utils import CustomException, filter_by_title_class, get_paginated_data, get_sort_keys, response, sort_data

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/titles")
async def get_all_titles(
    title_class: str = Query(None),
    _sort: str = Query(None),
    _order: str = Query('asc'),
    _page: int = Query(1, ge=1),
    _limit: int = Query(None, ge=1, le=100),
) -> dict[str, Union[str, str, List[TitleBasic]]]:
    try:
        # Mock database call
        titles_data = await call_database()

        # Filter by title_class if specified
        filtered_titles = filter_by_title_class(titles_data, title_class)

        # Parse _sort and _order query parameters
        sort_params = [param.lower() for param in _sort.split(",")] if _sort else []
        order_params = [param.lower() for param in _order.split(",")] if _order else []

        # Create a list of tuples (key, reverse) to pass to sorted()
        sort_keys = get_sort_keys(sort_params, order_params)

        # Sort the list using multiple keys (default = asc)
        sorted_titles = sort_data(filtered_titles, sort_keys)

        # Apply pagination
        paginated_titles = get_paginated_data(sorted_titles, _page, _limit)

        return response(success=True, data=paginated_titles)
    except:
        raise


@app.get("/api/titles/{id}")
async def get_title(id: int = Path(ge=0)) -> dict[str, Union[str, Title]]:
    try:
        # Mock database call
        title = await call_database(id)
        return response(data=title)
    except:
        raise


@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.code,
        content=exc.response
    )
