from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    id: str
    storage_id: str
    parent_class: str
    image_urls: List[str]
