import math
from PIL import Image


def calculate_entropy(image_path):
    """
    Calculates Shannon entropy of a grayscale image.
    """

    # 1. Open image
    image = Image.open(image_path)

    # 2. Convert to grayscale
    grayscale_image = image.convert("L")

    # 3. Get pixel values (0–255)
    pixels = list(grayscale_image.getdata())

    total_pixels = len(pixels)

    # 4. Count frequency of each pixel value
    frequency = {}
    for pixel in pixels:
        if pixel in frequency:
            frequency[pixel] += 1
        else:
            frequency[pixel] = 1

    # 5. Calculate entropy using Shannon formula
    entropy = 0
    for count in frequency.values():
        probability = count / total_pixels
        entropy -= probability * math.log2(probability)

    return entropy


if __name__ == "__main__":
    # Temporary testing
    clean_image = "samples/clean/clean-img.jpeg"
    stego_image = "samples/stego/test_stego_big.png"

    clean_entropy = calculate_entropy(clean_image)
    stego_entropy = calculate_entropy(stego_image)

    print("Clean Image Entropy:", clean_entropy)
    print("Stego Image Entropy:", stego_entropy)
