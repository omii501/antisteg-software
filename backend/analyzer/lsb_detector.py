from PIL import Image


def lsb_statistics(image_path):
    """
    Extracts LSB statistics from a grayscale image.
    Returns count of 0s, count of 1s, and their ratios.
    """

    # 1. Open image
    image = Image.open(image_path)

    # 2. Convert to grayscale
    grayscale = image.convert("L")

    # 3. Get pixel values
    pixels = list(grayscale.getdata())

    lsb_zeros = 0
    lsb_ones = 0

    # 4. Extract LSB from each pixel
    for pixel in pixels:
        lsb = pixel & 1   # bitwise AND to get LSB
        if lsb == 0:
            lsb_zeros += 1
        else:
            lsb_ones += 1

    total = lsb_zeros + lsb_ones

    zero_ratio = lsb_zeros / total
    one_ratio = lsb_ones / total

    return {
        "zeros": lsb_zeros,
        "ones": lsb_ones,
        "zero_ratio": zero_ratio,
        "one_ratio": one_ratio
    }


if __name__ == "__main__":
    # Temporary testing
    clean_image = "samples/clean/clean-img.jpeg"
    stego_image = "samples/stego/test_stego_big.png"

    clean_stats = lsb_statistics(clean_image)
    stego_stats = lsb_statistics(stego_image)

    print("Clean Image LSB Stats:", clean_stats)
    print("Stego Image LSB Stats:", stego_stats)
