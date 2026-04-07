def make_decision(risk_score):
    """
    Decide action based on risk score

    Returns:
        str: 'ALLOW', 'MASK', or 'DENY'
    """

    if risk_score >= 15:
        return "DENY"
    elif risk_score >= 8:
        return "MASK"
    else:
        return "ALLOW"