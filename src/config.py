import os

class Config:
    SECRET_KEY = os.urandom(24).hex()
    SESSION_TYPE = 'filesystem'
    GENAI_API_KEY = "AIzaSyAH7POcFUh2rVr8oqy5PzAekvXlAebXrYo"
