from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import os
from pathlib import Path


app = FastAPI()


@app.get("/")
def greet():
    return {"message": "bonjour"}