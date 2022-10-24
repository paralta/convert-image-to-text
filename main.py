import cv2
import pytesseract

image = cv2.imread('test.png')

text = pytesseract.image_to_string(image)
print(text)