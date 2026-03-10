import qrcode
import os

def generate_qr_code(url, file_name):
    """
    Generates a QR code for a given URL and saves it as an image.
    """

    try:
        # Ensure the folder exists
        folder = os.path.dirname(file_name)
        os.makedirs(folder, exist_ok=True)

        # Create QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        # Add data
        qr.add_data(url)
        qr.make(fit=True)

        # Create image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save image
        img.save(file_name)

        print(f"QR Code saved as {file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")


url_to_generate = "https://example.com"
file_name = "./qr_codes/name.png"

generate_qr_code(url_to_generate, file_name)




# for i in range(1, 101):
#     url = f"https://example.com/{i}"
#     file = f"./qr_codes/scan_{i}.png"
#     generate_qr_code(url, file)
