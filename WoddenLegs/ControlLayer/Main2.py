from ControlLayer.PDFReader import *
class Main2(object):
    """description of class"""

    def main(paths):
        print("Running main method")
        
        for path in paths:
            textDict = PDFReader.readImages(path)
            for page in textDict:
                print(page)

    if __name__ == '__main__':
        main()

