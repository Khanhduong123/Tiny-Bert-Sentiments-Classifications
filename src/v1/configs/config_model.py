import os
from dotenv import load_dotenv
load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_PREFIX = os.getenv("S3_PREFIX")