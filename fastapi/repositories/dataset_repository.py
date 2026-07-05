from fastapi import Depends
from fastapi.models import Dataset

class DatasetRepository:
    def get_dataset(self, dataset_id: int):
        # implement database query to get dataset
        pass
    def create_dataset(self, dataset: Dataset):
        # implement database query to create dataset
        pass