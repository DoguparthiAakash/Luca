from fastapi import APIRouter, Depends
from fastapi.schemas import ModelSchema
from fastapi.repositories import ModelRepository

model_router = APIRouter()

model_repository = ModelRepository()

@model_router.post("/models/")
async def create_model(model: ModelSchema):
    return model_repository.create_model(model)