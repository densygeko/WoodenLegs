from ControlLayer.PDFReader import *
class Main2(object):
    """description of class"""

    def main():
        print("Running main method")
        paths = ['ControlLayer\\TempPDFHolder\\OCRTestPDF.pdf', 'ControlLayer\\TempPDFHolder\\TestPDF2.pdf']

        for path in paths:
            textDict = PdfReader.readImages(path)
            for page in textDict:
                print(textDict[page])

    if __name__ == '__main__':
        main()

