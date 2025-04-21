import os
import sys
from flask import Flask, render_template
from flask_session import Session
from flask_cors import CORS

# Ensure Flask finds the 'src' folder
sys.path.append("src")

# Import blueprints
from routes.analyze import analyze_bp
from routes.history import history_bp

app = Flask(__name__, template_folder='templates')

# Session Configuration
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

CORS(app)

# Register Blueprints
app.register_blueprint(analyze_bp, url_prefix="/analyze")
app.register_blueprint(history_bp, url_prefix="/history")

# ✅ Route for index.html
@app.route("/")
def index():
    return render_template("index.html")

# ✅ Route for dashboard.html
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
