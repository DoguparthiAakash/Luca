from fastapi import APIRouter, Depends
from fastapi.schemas import DatasetSchema
from fastapi.repositories import DatasetRepository

dataset_router = APIRouter()

dataset_repository = DatasetRepository()

dataset_router.post("/datasets/")
async def create_dataset(dataset: DatasetSchema):
    return dataset_repository.create_dataset(dataset)