from PIL import Image


def chi_square_lsb(image_path):
    """
    Performs chi-square test on LSB distribution of an image.
    Returns chi-square value.
    """

    image = Image.open(image_path)
    grayscale = image.convert("L")
    pixels = list(grayscale.getdata())

    zeros = 0
    ones = 0

    for pixel in pixels:
        if pixel & 1 == 0:
            zeros += 1
        else:
            ones += 1

    total = zeros + ones

    expected = total / 2

    chi_square = ((zeros - expected) ** 2) / expected + \
                 ((ones - expected) ** 2) / expected

    return chi_square


if __name__ == "__main__":
    clean_image = "samples/clean/clean-img.jpeg"
    stego_image = "samples/stego/test_stego_big.png"

    clean_chi = chi_square_lsb(clean_image)
    stego_chi = chi_square_lsb(stego_image)

    print("Clean Image Chi-Square:", clean_chi)
    print("Stego Image Chi-Square:", stego_chi)
