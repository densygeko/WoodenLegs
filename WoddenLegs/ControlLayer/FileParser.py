from ControlLayer.PDFReader import *
from ControlLayer.RegexChecker import *
from ControlLayer.PCAPReader import *
from ControlLayer.TxtReader import *
from ControlLayer.CsvReader import *
from ControlLayer.ImgReader import *
from ModelLayer.Identifier import *

class FileParser: #Might want to refactor this class, as there is a lot of repeated code.

    def ParsePDF(self, paths):
        id = 0 #Id gets incremented when searching for identifiers and attached to them
        identifiers = []
        pdfReader = PdfReader()
        regex = RegexChecker()
        for path in paths:
            textDict = pdfReader.readImages(path) #Gets all normal text and text on images from PDF
            for page in textDict:
                
                emails = regex.checkMail(textDict[page]) #Find all emails using RegEx
                for email in emails:
                    ident = Identifier(email, "Email", path, page, id)
                    identifiers.append(ident) #Add email identifiers to list
                    id +=1
                
                phoneNumbers = regex.checkPhone(textDict[page])  #Find all danish phone numbers using RegEx
                for number in phoneNumbers:
                    ident = Identifier(number, "Telefon Nr.", path, page, id)
                    identifiers.append(ident) #Add phone number identifiers to list
                    id +=1

                ips = regex.findIP(textDict[page]) #Find all IPv4 and IPv6 addresses using RegEx
                for ip in ips:
                    ident = Identifier(str(ip), "IP-adresse", path, page, id)
                    identifiers.append(ident) #Add IP address identifiers to list
                    id +=1

        return identifiers
    
    def ParseImg(self, paths):
        id = 0
        identifiers = []
        imRead = ImgReader()
        regex = RegexChecker()
        for path in paths:
            img = imRead.ReadFile(path)
            emails = regex.checkMail(img)
            for email in emails:
                ident = Identifier(email, "Email", path, 0, id)
                identifiers.append(ident)
                id+=1

            phoneNumbers = regex.checkPhone(img)
            for number in phoneNumbers:
                ident = Identifier(number, "Telefon Nr.", path, 0, id)
                identifiers.append(ident)
                id+=1

            ips = regex.findIP(img)
            for ip in ips:
                ident = Identifier(str(ip), "IP-adresse", path, 0, id)
                identifiers.append(ident)
                id+=1
        return identifiers

    def ParseCsv(self, paths):
        id = 0
        identifiers = []
        csvReader = CsvReader()
        regex = RegexChecker()
        for path in paths:
            csvRows = csvReader.ReadFile(path)
            for row in csvRows:
                #Search for email
                emails = regex.checkMail(str(row))
                for email in emails:
                    ident = Identifier(email, "Email", path, 0, id)
                    identifiers.append(ident)
                    id+=1
                #Search for phone numbers
                phoneNumbers = regex.checkPhone(str(row))
                for number in phoneNumbers:
                    ident = Identifier(number, "Telefon Nr.", path, 0, id)
                    identifiers.append(ident)
                    id+=1
                #Search for IP addresses
                ips = regex.findIP(str(row))
                for ip in ips:
                    ident = Identifier(str(ip), "IP-adresse", path, 0, id)
                    identifiers.append(ident)
                    id+=1
        return identifiers

        
    def ParseTxt(self, paths):
        id = 0
        identifiers = []
        txtReader = TxtReader()
        regex = RegexChecker()
        for path in paths:
            data = txtReader.ReadFile(path)
            emails = regex.checkMail(data)
            for email in emails:
                ident = Identifier(email, "Email", path, 0, id)
                identifiers.append(ident)
                id+=1

            phoneNumbers = regex.checkPhone(data)
            for number in phoneNumbers:
                ident = Identifier(number, "Telefon Nr.", path, 0, id)
                identifiers.append(ident)
                id+=1

            ips = regex.findIP(data)
            for ip in ips:
                ident = Identifier(str(ip), "IP-adresse", path, 0, id)
                identifiers.append(ident)
                id+=1

        return identifiers
        
    def ParsePcap(self, paths):
        id = 0
        identifiers = []
        pcapReader = PCAPReader()
        for path in paths:
            ips = pcapReader.ReadFile(path)
            for ip in ips:
                ident = Identifier(str(ip), "IP-adresse", path, 0, id)
                identifiers.append(ident)
                id+=1
        
        return identifiers

    
