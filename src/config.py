from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()


API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing! Please set it in the .env file.")


genai.configure(api_key=API_KEY)
