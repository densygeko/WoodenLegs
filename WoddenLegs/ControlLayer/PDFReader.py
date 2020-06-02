import PyPDF4
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = os.getcwd() + r'\\Tesseract-OCR\\tesseract.exe'
import numpy as np
from PIL import Image

class PdfReader:
    def readImages(self, filepath):
        file = open(filepath, 'rb') #Open PDF
        fileReader = PyPDF4.PdfFileReader(file)
        pageTextDict = {}
        

        for i in range(fileReader.getNumPages()): #Run this code once for each page in PDF file
            page = fileReader.getPage(i) #Specify page to read
            text = "" #This will contain the text on the current page

            try:
                xObject = page['/Resources']['/XObject'].getObject() #Gets list of elements in page
            
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image': #If element is an image, resize and set color mode
                        size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                        data = xObject[obj].getData()
                        if(xObject[obj]['/ColorSpace'] == '/DeviceRGB'):
                            mode = "RGB"
                        else:
                            mode = "p"
            
                        if xObject[obj]['/Filter'] == '/FlateDecode':
                            img = Image.frombytes(mode, size, data) #Decode bytes and create image
                            img.save(obj[1:] + ".png")
                            text += pytesseract.image_to_string(img) + " " #Read any text in image
                  

                        elif xObject[obj]['/Filter'] == '/DCTDecode':
                            img = open(obj[1:] + ".jpg", "wb")
                            img.write(data) #Save image in project directory
                            img = Image.open(obj[1:] + ".jpg").convert('RGB') #Open and convert image
                            open_cv_image = np.array(img)
                            open_cv_image = open_cv_image[:, :, ::-1].copy() #Change image type to opencv from PIL
                            text += pytesseract.image_to_string(img) + " " #Read any text in image and add to text str
                            img.close()

                        elif xObject[obj]['/Filter'] == '/JPXDecode': #Haven't found anything to test this with, so it might not work
                            img = open(obj[1:] + ".jp2", "wb")
                            img.write(data)
                            #Change image type to opencv
                            img = Image.open(obj[1:] + ".jp2").convert('RGB')
                            open_cv_image = np.array(img)
                            open_cv_image = open_cv_image[:, :, ::-1].copy() #Change image type to opencv
                            text += pytesseract.image_to_string(img) + " " #Read any text in image and add to text str
                            img.close()

            except:
                print("No readable image in PDF")

            text += page.extractText()
            pageTextDict[i] = text

        file.close()
        return pageTextDict

#pdfRead = PdfReader()
#text = pdfRead.readImages('C:\\Users\\PhilipBraarup\\Desktop\\4thSemProject\\WoddenLegs\WoddenLegs\\ControlLayer\\TempPDFHolder\\quisquam.pdf')
#print(text)