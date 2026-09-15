def explain_warnings(warnings):
    """
    Creates simple explanations for each detected warning sign.
    """

    explanations = []

    for warning in warnings:

        if warning == "Urgent or threatening language":
            explanations.append(
                "This message pressures you to act quickly. "
                "Scammers often create urgency so you do not have time to verify the message."
            )

        elif warning == "Request involving money or payment":
            explanations.append(
                "This message involves money or a payment request. "
                "Be careful before sending money or purchasing something."
            )

        elif warning == "Request for personal or financial information":
            explanations.append(
                "This message asks for sensitive information. "
                "Legitimate organizations generally should not ask you to provide "
                "passwords or security codes through suspicious messages."
            )

        elif warning == "Potentially suspicious link or login request":
            explanations.append(
                "This message may be trying to get you to click a link or log in. "
                "Avoid clicking suspicious links and visit the organization's official website instead."
            )

    return explanations
