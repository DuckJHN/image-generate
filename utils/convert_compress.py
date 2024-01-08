import cv2 as cv


def convert_and_compress(image, output_path, format='jpeg', compression_level=0):

    if format.lower() not in ['jpeg', 'png', 'jpg']:
        print(f"Error: Unsupported format '{format}'. Chosse again")
        return

    if format in ['JPEG', 'JPG']:
        # JPEG format (compression_level ranges from 0 to 100)
        compression_params = [int(
            cv.IMWRITE_JPEG_QUALITY), compression_level] if compression_level is not None else None
    elif format == 'PNG':
        # PNG format (compression_level ranges from 0 to 9)
        compression_params = [int(cv.IMWRITE_PNG_COMPRESSION),
                              compression_level] if compression_level is not None else None

    success = cv.imwrite(output_path, image, compression_params)

    if success:
        print(
            f"Image saved successfully to '{output_path}' in {format} format.")
    else:
        print(f"Error: Failed to save image to '{output_path}'.")


# img = cv.imread("nft2.jpg")

# convert_and_compress(img, "output.jpg", format='JPEG', compression_level=1)

# convert_and_compress(img, "output.png", format='PNG', compression_level=0)
