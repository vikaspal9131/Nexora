from flask import Blueprint

analyze_bp = Blueprint('analyze', __name__)
history_bp = Blueprint('history', __name__)

from . import analyze, history
