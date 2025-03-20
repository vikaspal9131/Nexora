from flask import Flask
from flask_session import Session
from dotenv import load_dotenv
import os
from routes import api  

load_dotenv()  

app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your_default_secret_key")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = os.path.join(os.getcwd(), "sessions")


if not os.path.exists(app.config["SESSION_FILE_DIR"]):
    os.makedirs(app.config["SESSION_FILE_DIR"])


Session(app)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
