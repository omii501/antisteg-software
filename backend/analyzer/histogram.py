from PIL import Image


def image_histogram(image_path):
    """
    Calculates grayscale histogram of an image.
    Returns a list of 256 values (frequency of each pixel value).
    """

    image = Image.open(image_path)
    grayscale = image.convert("L")
    pixels = list(grayscale.getdata())

    histogram = [0] * 256

    for pixel in pixels:
        histogram[pixel] += 1

    return histogram


def histogram_difference(hist1, hist2):
    """
    Calculates absolute difference between two histograms.
    """

    diff = 0
    for i in range(256):
        diff += abs(hist1[i] - hist2[i])

    return diff


if __name__ == "__main__":
    clean_image = "samples/clean/clean-img.jpeg"
    stego_image = "samples/stego/test_stego_big.png"

    clean_hist = image_histogram(clean_image)
    stego_hist = image_histogram(stego_image)

    diff = histogram_difference(clean_hist, stego_hist)

    print("Histogram difference:", diff)
