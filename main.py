from detector import analyze_message
from risk_score import calculate_risk_score, get_risk_level
from explanations import explain_warnings


def main():
    print("=" * 40)
    print("          SENIORSHIELD")
    print("=" * 40)
    print()
    print("Paste a message below to check for")
    print("potential scam warning signs.")
    print()

    message = input("Message: ")

    if not message.strip():
        print("\nPlease enter a message to analyze.")
        return

    print("\nAnalyzing message...")

    warnings = analyze_message(message)
    score = calculate_risk_score(warnings)
    risk_level = get_risk_level(score)
    explanations = explain_warnings(warnings)

    print("\n" + "=" * 40)
    print(f"RISK LEVEL: {risk_level}")
    print(f"RISK SCORE: {score}/100")
    print("=" * 40)

    if warnings:
        print("\nWARNING SIGNS:")

        for warning in warnings:
            print(f"- {warning}")

        print("\nWHY IT WAS FLAGGED:")

        for explanation in explanations:
            print(f"- {explanation}")

        print("\nRECOMMENDATION:")
        print("Be cautious. Do not click suspicious links or")
        print("send personal information or money until you")
        print("can verify who contacted you.")

    else:
        print("\nNo common warning signs were detected.")
        print("However, this does not guarantee that the")
        print("message is safe.")

    print("\nThank you for using SeniorShield.")


if __name__ == "__main__":
    main()
