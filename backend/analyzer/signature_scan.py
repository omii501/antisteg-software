def signature_scan(file_path):
    """
    Scans a file for known steganography-related signatures
    and suspicious embedded patterns.
    """

    findings = []

    with open(file_path, "rb") as f:
        data = f.read()

    # Convert binary to lowercase string for keyword search
    try:
        data_text = data.decode(errors="ignore").lower()
    except:
        data_text = ""

    # 1️⃣ Known steganography tool signatures
    stego_keywords = [
        "stegano",
        "steghide",
        "openstego",
        "lsb",
        "hidden message"
    ]

    for keyword in stego_keywords:
        if keyword in data_text:
            findings.append(f"Found steganography keyword: {keyword}")

    # 2️⃣ Suspicious embedded file headers
    magic_signatures = {
        b"PK\x03\x04": "ZIP archive",
        b"%PDF": "PDF document",
        b"MZ": "Windows executable",
    }

    for magic, description in magic_signatures.items():
        if magic in data:
            findings.append(f"Embedded file signature detected: {description}")

    # 3️⃣ Large readable ASCII text block (simple heuristic)
    readable_chars = sum(c in range(32, 127) for c in data)
    readable_ratio = readable_chars / len(data)

    if readable_ratio > 0.3:
        findings.append("Unusually high readable text content inside binary file")

    return findings


if __name__ == "__main__":
    test_file = "samples/stego/test_stego_big.png"

    results = signature_scan(test_file)

    if results:
        print("Signature scan findings:")
        for r in results:
            print("-", r)
    else:
        print("No known signatures detected.")
