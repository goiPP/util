import base64


def decode():
    # Replace 'string' with your base64 encoded string
    encoded_string = """encoded jks>"""

    # Write the decoded bytes to a.jks file
    with open("dev/decoded.jks", "wb") as file:
        file.write(decoded_bytes)


def encode():
    # Read the contents of a.jks file
    with open("cert/ssl.jks", "rb") as file:
        # with open('dev/a.jks', 'rb') as file:
        jks_bytes = file.read()

    # Encode the bytes to base64 format
    encoded_string = base64.b64encode(jks_bytes).decode("utf-8")

    # Print or use the encoded string as needed
    print(encoded_string)


if __name__ == "__main__":
    encode()
