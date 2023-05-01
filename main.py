from typing import List
from fastapi import FastAPI, Query
from database import call_database
from title import TitleBasic
from utils import filter_by_title_class

app = FastAPI()

@app.get("/api/titles")
async def get_all_titles(
    title_class: str = Query(None),
) -> List[TitleBasic]:
    try:
        # Mock database call
        titles_data = await call_database()

        # Filter by title_class if specified
        filtered_titles = filter_by_title_class(titles_data, title_class)
        return filtered_titles
    except:
        raise