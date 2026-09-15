def calculate_risk_score(warnings):
    """
    Calculates a risk score based on detected warning signs.
    Returns a score between 0 and 100.
    """

    points = {
        "Urgent or threatening language": 20,
        "Request involving money or payment": 30,
        "Request for personal or financial information": 25,
        "Potentially suspicious link or login request": 25
    }

    score = 0

    for warning in warnings:
        score += points.get(warning, 0)

    return min(score, 100)


def get_risk_level(score):
    """
    Converts the numerical score into a risk level.
    """

    if score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    else:
        return "LOW"
