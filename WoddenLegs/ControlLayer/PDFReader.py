import PyPDF4
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import numpy as np
from PIL import Image

def readPDF():
    file = open('ControlLayer\\TempPDFHolder\\report.pdf', 'rb') #Open PDF
    fileReader = PyPDF4.PdfFileReader(file)

    page = fileReader.getPage(0) #Specify page to read

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
                text = pytesseract.image_to_string(img) #Read any text in image
                print(text)
                

            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(obj[1:] + ".jpg", "wb")
                img.write(data) #Save image in project directory
                
                #Change image type to opencv
                img = Image.open('Im7.jpg').convert('RGB') #Open and convert image (this is hardcoded, needs to be fixed)
                open_cv_image = np.array(img)
                open_cv_image = open_cv_image[:, :, ::-1].copy()

                text = pytesseract.image_to_string(img) #Read any text in image
                print(text)
                img.close()

            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(obj[1:] + ".jp2", "wb")
                img.write(data)

                #Change image type to opencv
                img = Image.open('Im7.jpg').convert('RGB')
                open_cv_image = np.array(img)
                open_cv_image = open_cv_image[:, :, ::-1].copy() 

                text = pytesseract.image_to_string(img) #Read any text in image
                print(text)
                img.close()



readPDF()