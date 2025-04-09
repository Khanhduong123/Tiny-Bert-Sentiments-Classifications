from fastapi import APIRouter
from .v1.router.predict import router as PredictSentences

api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(PredictSentences)