from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()

with open("emails", "a") as f:
    f.write("")

@app.get("/")
async def root():
    with open("sometext", "a") as f:
        f.write("something\n")

    with open("sometext", "r") as f:
        s = f.read()
        return {"message": s}


@app.get("/emailCollect/{email}")
async def emailCollect(email: str):
    with open("emails", "a") as f:
        f.write(email + "\n")
    return "good"

@app.get("/emails")
async def emails():
    with open("emails", "r") as f:
        emails = f.readlines()
        return {"emails": emails}
