"""Module to convert image to text using CLI."""
import sys
import cv2 # pylint: disable=import-error
import pytesseract # pylint: disable=import-error

image = cv2.imread(sys.argv[1])

text = pytesseract.image_to_string(image)
print(text)
