from ControlLayer.PDFReader import *
from ControlLayer.RegexChecker import *
from ModelLayer.Identifier import *
import sys

class Main2():

    def main():
        print("Running main method")
        paths = ['ControlLayer\\TempPDFHolder\\TestPDF.pdf', 'ControlLayer\\TempPDFHolder\\TestPDF2.pdf']

        for arg in sys.argv[1:]:
            print(arg)

        id = 0
        identifiers = []
        for path in paths:
            textDict = PdfReader.readImages(path)
            for page in textDict:
                
                emails = RegexChecker.checkMail(textDict[page])
                for email in emails:
                    ident = Identifier(email, "Email", path, page, id)
                    identifiers.append(ident)
                    id +=1
                
                phoneNumbers = RegexChecker.checkPhone(textDict[page])
                for number in phoneNumbers:
                    ident = Identifier(number, "PhoneNumber", path, page, id)
                    identifiers.append(ident)
                    id +=1

                ips = RegexChecker.findIP(textDict[page])
                for ip in ips:
                    ident = Identifier(number, "IP", path, page, id)
                    identifiers.append(ident)
                    id +=1

        for identifier in identifiers:
            print("\nID: " + str(identifier.id) + "\nIdentifier: " + identifier.name + "\nPage:" + str(identifier.page) + "\nPath:" + identifier.path + "\nType:" + identifier.type)

    if __name__ == '__main__':
        main()

