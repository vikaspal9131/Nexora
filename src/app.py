import os
import sys
from flask import Flask
from flask_session import Session

# Ensure Flask finds the 'src' folder
sys.path.append("src")

# Import blueprints
from routes.analyze import analyze_bp
from routes.history import history_bp

app = Flask(__name__)

# Session Configuration
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Register Blueprints
app.register_blueprint(analyze_bp, url_prefix="/analyze")
app.register_blueprint(history_bp, url_prefix="/history")

@app.route("/")
def home():
    return "Resume Analyzer API is running!"

if __name__ == "__main__":
    app.run(debug=True)
