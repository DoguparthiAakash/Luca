from fastapi import Depends
from fastapi.models import Model

class ModelRepository:
    def get_model(self, model_id: int):
        # implement database query to get model
        pass
    def create_model(self, model: Model):
        # implement database query to create model
        pass