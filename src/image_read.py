from PIL import Image
import os
import easyocr


def read_image():
    path = input("Enter the path of image file: ")
    path = path.strip('"')

    try:
        # Check if  file exists
        if not os.path.isfile(path):
            raise FileNotFoundError(f"No file found at: {path}")

        # Open  image
        image = Image.open(path)
        image.show()  # Opens the image in viewer
        # OCR got this from web
        reader = easyocr.Reader(['en'])
        result = reader.readtext(path, detail=0)

        print("Extracted text from image:")
        for line in result:
            print(line)

    except FileNotFoundError as e:
        print(e)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    read_image()
