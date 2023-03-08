from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    if_offer: Union[bool, None] = None