import argparse
import os

from backend.core.file_loader import load_file
from backend.core.decision_engine import decide_risk

from backend.analyzer.entropy import calculate_entropy
from backend.analyzer.lsb_detector import lsb_statistics
from backend.analyzer.chi_square_test import chi_square_lsb
from backend.analyzer.histogram import image_histogram
from backend.analyzer.signature_scan import signature_scan


def analyze_file(file_path):
    file_info = load_file(file_path)

    entropy = calculate_entropy(file_path)

    lsb_stats = lsb_statistics(file_path)
    lsb_deviation = abs(lsb_stats["zero_ratio"] - 0.5)

    chi_square = chi_square_lsb(file_path)

    histogram = image_histogram(file_path)
    histogram_diff = sum(abs(v - (sum(histogram) / 256)) for v in histogram)

    signatures = signature_scan(file_path)

    analysis_results = {
        "entropy": entropy,
        "chi_square": chi_square,
        "histogram_diff": histogram_diff,
        "lsb_deviation": lsb_deviation,
        "signatures": signatures
    }

    return decide_risk(analysis_results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AntiSteg - Steganography Detection Tool"
    )
    parser.add_argument("file", help="Path to file to scan")
    args = parser.parse_args()

    file_path = os.path.abspath(args.file)

    try:
        result = analyze_file(file_path)

        print("\nFinal Scan Result")
        print("-----------------")
        print("Risk Level:", result["risk_level"])
        print("Risk Score:", result["risk_score"])
        print("Reasons:")
        for r in result["reasons"]:
            print("-", r)

    except FileNotFoundError:
        print("Error: File not found.")
