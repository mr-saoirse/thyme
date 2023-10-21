from pydantic import BaseModel, Field
import typing


class Author(BaseModel):
    """
    If we have sub types that are fixed in structure we can add them
    often its better just to use a dictionary for a bag of attributes
    """

    name: str
    email: typing.Optional[str]


class Recipe(BaseModel):
    """
    This is an example pydantic object
    The type inference and possible "hints" in the fields are important!
    """

    # when we have primary key fields and the user tells is its a key we can add this Field attribute
    id: int = Field(is_key=True)
    name: str
    cuisine: str
    # ingredients usually in
    ingredients: typing.List[str]
    instructions: str = Field(large_text=True)
    # fields that we think are numeric can have a hint e.g. is_numeric=True. We would not add is_numeric=False anywhere which is assumed default
    rating: float = Field(is_numeric=True)
    cooking_time: int = Field(is_numeric=True)
    # we can usually add a bag of attributes as an optional dict
    # some data may require a child type if we think the structure is fixed
    metadata = typing.Optional[dict]
    author: typing.Optional[Author]
