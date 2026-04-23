from fastapi import FastAPI
from .scraper import fetch_page

app =  FastAPI()

@app.get("/scrape")
def scrape(url: str):
    data = fetch_page(url)
    return {"url":url, "data":data}