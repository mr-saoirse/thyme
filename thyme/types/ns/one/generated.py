
from enum import Enum
from pydantic import BaseModel, root_validator, validator
from typing import List

class KanbanStage(Enum):
    ToDo = 'ToDo'
    Done = 'Done'
    InProgress = 'InProgress'
    Blocked = 'Blocked'

class Kanban(BaseModel):
    stage: KanbanStage = KanbanStage.ToDo

    class Config:
        schema_extra = {
            "example": {
                "stage": "ToDo"
            }
        }

    @root_validator(pre=True)
    def check_stage(cls, values):
        assert 'stage' in values, 'stage must be provided'
        assert values['stage'] == KanbanStage.ToDo, 'stage must be ToDo by default'
        return values

class Task(BaseModel):
    name: str
    kanban: Kanban

    class Config:
        schema_extra = {
            "example": {
                "name": "Design layer architecture",
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
                "name": "Mary Johnson",
                "tasks": [
                    {
                        "name": "Set up deployment pipeline",
                        "kanban": {
                            "stage": "ToDo"
                        }
                    }
                ]
            }
        }
