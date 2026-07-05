from pydantic import BaseModel

class ModelSchema(BaseModel):
    name: str
    dataset_id: int