from pydantic import BaseModel

class Model(BaseModel):
    id: int
    name: str
    dataset_id: int