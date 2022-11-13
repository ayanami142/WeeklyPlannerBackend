from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends

from config import Settings

app = FastAPI()


@lru_cache()
def get_settings() -> Settings:
    """
    Get Settings instance
    :return: Settings
    """
    return Settings()


@app.get("/settings")
async def root(settings: Settings = Depends(get_settings)) -> dict:
    if settings.DEBUG:
        response = {key: value for key, value in vars(settings).items()}

        return response


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
