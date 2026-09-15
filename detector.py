def analyze_message(message):
    """
    Analyzes a message for common scam and phishing warning signs.
    Returns a list of detected warning signs.
    """

    message = message.lower()
    warnings = []

    urgent_words = [
        "urgent",
        "immediately",
        "act now",
        "right away",
        "expires today",
        "final warning"
    ]

    money_words = [
        "send money",
        "payment",
        "gift card",
        "wire transfer",
        "cash app",
        "venmo",
        "bitcoin"
    ]

    personal_info_words = [
        "password",
        "social security",
        "bank account",
        "credit card",
        "security code",
        "verification code"
    ]

    suspicious_link_words = [
        "click here",
        "click the link",
        "verify your account",
        "login here"
    ]

    if any(word in message for word in urgent_words):
        warnings.append("Urgent or threatening language")

    if any(word in message for word in money_words):
        warnings.append("Request involving money or payment")

    if any(word in message for word in personal_info_words):
        warnings.append("Request for personal or financial information")

    if any(word in message for word in suspicious_link_words):
        warnings.append("Potentially suspicious link or login request")

    return warnings
