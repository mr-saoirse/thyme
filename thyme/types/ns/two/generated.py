
from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    type: str
    author: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Easy Salad",
                "type": "Salad",
                "author": "Chefkoch"
            }
        }
