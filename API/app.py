import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows


@app.get("/cursosPlatzi")
def get_cursos():
    rows = ["Docker", "Bash", "Linux", "Inglés", "Python", "Javascript", "Shazam", "Azure"]
    return rows