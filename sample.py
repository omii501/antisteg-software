from PIL import Image

def extract_hidden_text():
    # 👇 Put your image path here
    image_path = "samples/stego/stegotest.jpg"   # example: "C:/Users/Hardik/Desktop/stego.png"

    img = Image.open(image_path)
    pixels = img.load()

    binary_data = ""
    decoded_text = ""

    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Extract LSB from each RGB channel
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

            # Convert every 8 bits to character
            if len(binary_data) >= 8:
                byte = binary_data[:8]
                binary_data = binary_data[8:]

                char = chr(int(byte, 2))
                decoded_text += char

                # Stop when delimiter is found
                if decoded_text.endswith("#####"):
                    print("Hidden Message Found:")
                    return decoded_text.replace("#####", "")

    return decoded_text


# 🔍 Run extraction
hidden_message = extract_hidden_text()
print(hidden_message)
