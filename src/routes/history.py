from flask import Blueprint, jsonify, session

history_bp = Blueprint('history', __name__)

@history_bp.route('/last_analysis', methods=['GET'])
def get_last_analysis():
    if 'last_analysis' in session:
        return jsonify({"last_analysis": session['last_analysis']})
    return jsonify({"error": "No previous analysis found"}), 404
