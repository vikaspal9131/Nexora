from flask import Blueprint

# Initialize Blueprint instances (optional, but helps with organization)
analyze_bp = Blueprint('analyze', __name__)
history_bp = Blueprint('history', __name__)

# Import route files to register their routes
from . import analyze, history
