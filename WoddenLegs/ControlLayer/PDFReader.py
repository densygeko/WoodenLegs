import PyPDF4
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import numpy as np

from PIL import Image

def readPDF():
    file = open('ControlLayer\\TempPDFHolder\\report.pdf', 'rb')
    fileReader = PyPDF4.PdfFileReader(file)

    page = fileReader.getPage(0)

    xObject = page['/Resources']['/XObject'].getObject()

    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj].getData()
            if(xObject[obj]['/ColorSpace'] == '/DeviceRGB'):
                mode = "RGB"
            else:
                mode = "p"

            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                img.save(obj[1:] + ".png")
                text = pytesseract.image_to_string(img)
                print(text)
                

            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(obj[1:] + ".jpg", "wb")
                img.write(data)
                
                img = Image.open('Im7.jpg').convert('RGB')
                open_cv_image = np.array(img)
                open_cv_image = open_cv_image[:, :, ::-1].copy()

                text = pytesseract.image_to_string(img)
                print(text)

                img.close()

            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(obj[1:] + ".jp2", "wb")
                img.write(data)

                img = Image.open('Im7.jpg').convert('RGB')
                open_cv_image = np.array(img)
                open_cv_image = open_cv_image[:, :, ::-1].copy()

                text = pytesseract.image_to_string(img)
                print(text)

                img.close()



readPDF()