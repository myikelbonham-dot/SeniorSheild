from scam_patterns import (
    URGENT_WORDS,
    MONEY_WORDS,
    PERSONAL_INFO_WORDS,
    SUSPICIOUS_LINK_WORDS
)


def analyze_message(message):
    """
    Analyzes a message for common scam and phishing warning signs.
    Returns a list of detected warning signs.
    """

    message = message.lower()
    warnings = []

    if any(word in message for word in URGENT_WORDS):
        warnings.append("Urgent or threatening language")

    if any(word in message for word in MONEY_WORDS):
        warnings.append("Request involving money or payment")

    if any(word in message for word in PERSONAL_INFO_WORDS):
        warnings.append("Request for personal or financial information")

    if any(word in message for word in SUSPICIOUS_LINK_WORDS):
        warnings.append("Potentially suspicious link or login request")

    return warnings
