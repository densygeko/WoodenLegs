import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = os.getcwd() + r'\\Tesseract-OCR\\tesseract.exe'
from PIL import Image

#This class reads text on images.
class ImgReader:
 
    def ReadFile(self, file):
        img = Image.open(file).convert('RGB') #Open file and convert to format that is compatible with pytesseract
        return pytesseract.image_to_string(img) #Return string with any text in the image

