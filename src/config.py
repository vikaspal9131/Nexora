import os

class Config:
    SECRET_KEY = os.urandom(24).hex()
    SESSION_TYPE = 'filesystem'
    GENAI_API_KEY = "AIzaSyA18kz5oa1jrrMcm7d9TJd3ekT2bgCkTsU"
