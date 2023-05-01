import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/titles")
async def get_all_titles():
    try:
        with open('data.json', 'r') as data:
            titles_data = json.load(data)
            return titles_data
    except:
        raise