from flask import Blueprint, request, jsonify
from database.db import get_connection
from services.risk_engine import calculate_risk
from services.decision_engine import make_decision

api_bp = Blueprint('api', __name__)


@api_bp.route('/analyze', methods=['POST'])
def analyze_request():
    """
    Analyze recruiter request and return decision
    """

    data = request.get_json()

    recruiter = data.get('recruiter')
    frequency = data.get('frequency', 0)
    denied = data.get('denied', 0)
    odd_time = data.get('odd_time', 0)
    unknown = data.get('unknown', 0)

    # Step 1: Calculate risk
    risk_score = calculate_risk(frequency, denied, odd_time, unknown)

    # Step 2: Make decision
    decision = make_decision(risk_score)

    # Step 3: Store in DB
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO requests 
        (recruiter, frequency, denied, odd_time, unknown, risk_score, decision)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (recruiter, frequency, denied, odd_time, unknown, risk_score, decision))

    conn.commit()
    conn.close()

    # Step 4: Return response
    return jsonify({
        "recruiter": recruiter,
        "risk_score": risk_score,
        "decision": decision
    })