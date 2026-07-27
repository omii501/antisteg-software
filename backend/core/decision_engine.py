analysis_results = {
    "entropy": 6.35,
    "chi_square": 4091.32,
    "histogram_diff": 296828,
    "lsb_deviation": 0.009,
    "signatures": [
        "Found steganography keyword: lsb",
        "Embedded file signature detected: Windows executable"
    ]
}

def decide_risk(analysis_results):
    """
    Combines analysis results and returns final risk level and reasons.
    """

    risk_score = 0
    reasons = []

    # --- Strong signals ---
    if analysis_results.get("chi_square", 0) > 1000:
        risk_score += 3
        reasons.append("Strong statistical deviation detected (chi-square test).")

    if analysis_results.get("signatures"):
        risk_score += 3
        reasons.append("Suspicious signatures found inside the file.")

    # --- Medium signals ---
    if analysis_results.get("histogram_diff", 0) > 100000:
        risk_score += 2
        reasons.append("Histogram shows abnormal pixel distribution.")

    if analysis_results.get("lsb_deviation", 0) > 0.005:
        risk_score += 2
        reasons.append("LSB bit distribution deviates from normal behavior.")

    # --- Weak signals ---
    entropy = analysis_results.get("entropy", 0)
    if entropy < 5.5 or entropy > 7.8:
        risk_score += 1
        reasons.append("Entropy value is unusual for a natural image.")

    # --- Final decision ---
    if risk_score >= 6:
        risk_level = "HIGH"
    elif risk_score >= 3:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "reasons": reasons
    }


if __name__ == "__main__":
    # Temporary test
    test_results = {
        "entropy": 6.35,
        "chi_square": 4091.32,
        "histogram_diff": 296828,
        "lsb_deviation": 0.009,
        "signatures": ["Found steganography keyword: lsb"]
    }

    decision = decide_risk(test_results)

    print("Risk Level:", decision["risk_level"])
    print("Risk Score:", decision["risk_score"])
    print("Reasons:")
    for r in decision["reasons"]:
        print("-", r)
