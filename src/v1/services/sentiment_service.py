import os
import torch
from transformers import pipeline
from src.v1.providers.s3_provider import download_model
from src.v1.configs.config_model import S3_BUCKET_NAME, S3_PREFIX

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
local_path = "src/v1/configs/checkpoints"  # Tùy chỉnh đường dẫn lưu mô hình

# Download mô hình từ S3
if os.path.exists(local_path):
    print(f"Model already exists at {local_path}. Skipping download.")
else:
    print(f"Downloading model from S3 to {local_path}...")
    download_model(S3_BUCKET_NAME, S3_PREFIX, local_path)

# Khởi tạo mô hình phân loại
classifier = pipeline('text-classification', model=local_path, device=device)

def predict_sentiment(text: str):
    prediction = classifier(text)
    return prediction[0]
