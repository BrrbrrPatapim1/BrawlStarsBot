
from pydantic import BaseModel
from typing import List, Union

class Guide(BaseModel):
    name: str
    rare: str
    gadget: str           # Виправлено: str замість float
    starpowers: List[str]
    gears: Union[str, List[str]] # Виправлено: додано підтримку рядка
