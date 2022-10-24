import cv2
import sys
import pytesseract

image = cv2.imread(sys.argv[1])

text = pytesseract.image_to_string(image)
print(text)
