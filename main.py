from typing import List
from fastapi import FastAPI

from database import call_database
from title import TitleBasic

app = FastAPI()

@app.get("/api/titles")
async def get_all_titles() -> List[TitleBasic]:
    try:
        # Mock database call
        titles_data = await call_database()
        return titles_data
    except:
        raise