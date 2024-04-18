from fastapi import FastAPI
from pydantic import BaseModel


class ML(BaseModel):
    item:str