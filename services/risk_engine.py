def calculate_risk(frequency, denied, odd_time, unknown):
    """
    Calculate risk score based on behavior patterns

    Formula:
    Risk = (Frequency × 2) + (Denied × 3) + (OddTime × 2) + (Unknown × 5)
    """

    risk_score = (
        (frequency * 2) +
        (denied * 3) +
        (odd_time * 2) +
        (unknown * 5)
    )

    return risk_score