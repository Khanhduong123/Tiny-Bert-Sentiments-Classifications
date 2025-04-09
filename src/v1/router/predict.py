from fastapi import APIRouter
from src.v1.models.sentiment_model import SentimentRequest, SentimentResponse
from src.v1.services.sentiment_service import predict_sentiment

router = APIRouter(prefix="/predict", tags=["predict"])

@router.post("/", response_model=SentimentResponse)
def predict_sentiment_route(request: SentimentRequest):
    result = predict_sentiment(request.text)
    return SentimentResponse(label=result['label'], score=result['score'])
