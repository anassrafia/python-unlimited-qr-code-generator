import qrcode

def generate_qr_code(url, file_name):
    """
    Generates a QR code for a given URL and saves it as an image.

    :param url: The URL to encode in the QR code.
    :param file_name: The name of the output file.
    """
    try:
        # Create QR code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
            box_size=10,  # Size of each box
            border=4,  # Thickness of the border
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create and save the image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)
        print(f"QR Code saved as {file_name}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage
# for i in range(7, 8):
#    url_to_generate = f"https://www.example.com/files"
#    file_name = f"./qr_codes/scan_{i}.png"
#    generate_qr_code(url_to_generate, file_name)


url_to_generate = f"https://example.com"
file_name = f"./qr_codes/name.png"
generate_qr_code(url_to_generate, file_name)