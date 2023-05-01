from fastapi import FastAPI

from database import call_database

app = FastAPI()

@app.get("/api/titles")
async def get_all_titles():
    try:
        # Mock database call
        titles_data = await call_database()
        return titles_data
    except:
        raise