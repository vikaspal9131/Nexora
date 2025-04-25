import os

class Config:
    SECRET_KEY = os.urandom(24).hex()
    SESSION_TYPE = 'filesystem'
    GENAI_API_KEY = "AIzaSyDSDK4CfwnJ4rKU3ssWA2iNaNyxhO3sp8"
