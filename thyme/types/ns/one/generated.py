
from enum import Enum
from pydantic import BaseModel, root_validator, Field
from typing import List, Optional

class Stage(Enum):
    ToDo = "ToDo"
    Done = "Done"
    InProgress = "InProgress"
    Blocked = "Blocked"


class Kanban(BaseModel):
    stage: Stage = Field(default=Stage.ToDo)

    @root_validator(pre=True)
    def default_stage(cls, values):
        if 'stage' not in values:
            values['stage'] = Stage.ToDo
        return values

    class Config:
        schema_extra = {
            "example": {
                "stage": "ToDo"
            }
        }


class Task(BaseModel):
    name: str
    description: Optional[str] = None
    kanban: Kanban

    class Config:
        schema_extra = {
            "example": {
                "name": "Test Task",
                "description": "This is a test task",
                "kanban": {
                    "stage": "ToDo"
                }
            }
        }


class Actor(BaseModel):
    name: str
    tasks: List[Task]

    class Config:
        schema_extra = {
            "example": {
                "name": "John",
                "tasks": [
                    {
                        "name": "Test Task",
                        "description": "This is a test task",
                        "kanban": {
                            "stage": "ToDo"
                        }
                    }
                ]
            }
        }
