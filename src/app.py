import os
import sys
from flask import Flask, render_template
from flask_session import Session
from flask_cors import CORS
from flask import Flask, request, redirect



sys.path.append("src")

from routes.analyze import analyze_bp
from routes.history import history_bp

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

CORS(app)


app.register_blueprint(analyze_bp, url_prefix="/analyze")
app.register_blueprint(history_bp, url_prefix="/history")




@app.route("/")
def index():
    return render_template("index.jinja")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.jinja")



@app.route("/login")
def login():
    return render_template("login.jinja")

@app.route("/template")
def template():
    return render_template("template.jinja")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
