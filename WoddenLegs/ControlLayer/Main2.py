from ControlLayer.PDFReader import *
from ControlLayer.RegexChecker import *
from ControlLayer.PCAPReader import *
from ControlLayer.TxtReader import *
from ModelLayer.Identifier import *
from ModelLayer.MatchedIdentifier import *
from xml.dom import minidom
import sys
import os
import ast
import threading
#import subprocess


class Main2():

    def MatchIdentifiers(self, identifiers):
        print("Beginning identifier matching")
        matchedIdentifiers = []
        print("Identifiers found: " + str(len(identifiers)))
        for i in identifiers: #Loop through each identifier.
            if i.isMatched == False: #Don't match the identifier if it has already been matched. This is to avoid creating duplicate matches
                match = None
                paths = [i.path] #List of paths the identifier is found in
                for j in identifiers: #Compare the identifier to every other identifier
                    if i.name == j.name and i.path != j.path: # Check if the same identifier is found in a different file
                        if j.path not in paths: #This avoids counting the same identifier multiple times from one document
                            paths.append(j.path)
                            if match == None: #Create MatchedIdentifier at first occurence of a matching identifier
                                match = MatchedIdentifier(i.name, i.type, paths, i.id, 1)
                            
                            match.occurences +=1 #At all following occurences of the same identifier, increment occurences
                            j.isMatched = True #The method won't loop through objects that have already been matched

                if match != None: #Only add match object to list if it has been instantiated
                    matchedIdentifiers.append(match)

        return matchedIdentifiers
    
    def CreateXMLDoc(self, identifiers):
        print("Creating XML DOC")
        print("Number of matched identifiers: " + str(len(identifiers)))
        root = minidom.Document() #Create XML Document
        xml = root.createElement('root')
        root.appendChild(xml)
        
        for identifier in identifiers:
            identifierChild = root.createElement('Identifier') #Append identifier as an element
            identifierChild.setAttribute('id', str(identifier.id))
            xml.appendChild(identifierChild)

            childOfIdentifier = root.createElement('name') #Create element 'name'
            childOfIdentifier.appendChild(root.createTextNode(identifier.name)) #Set content to identifier attribute
            identifierChild.appendChild(childOfIdentifier) #Attach element 'name' to 'Identifier'

            childOfIdentifier = root.createElement('paths')
            identifierChild.appendChild(childOfIdentifier)

            for path in identifier.paths:
                childOfPath = root.createElement('path')
                childOfPath.appendChild(root.createTextNode(path))
                childOfIdentifier.appendChild(childOfPath)

            childOfIdentifier = root.createElement('occurences')
            childOfIdentifier.appendChild(root.createTextNode(str(identifier.occurences)))
            identifierChild.appendChild(childOfIdentifier)

            childOfIdentifier = root.createElement('type')
            childOfIdentifier.appendChild(root.createTextNode(identifier.type))
            identifierChild.appendChild(childOfIdentifier)

        xml_str = root.toprettyxml(indent="\t") #Format XML

        currentDir = os.getcwd()
        save_path_file = currentDir + '\MatchedIdentifiers.xml' #Set document title + path
        with open(save_path_file, "w") as f: #Save XML doc
            f.write(xml_str)

    def main(self): #Needs to be updated to take a list of lists of paths

        if len(sys.argv) <= 1: #Must have at least one argument when executing this class in command line
            print("Please enter the path to the filepaths.xml document")
            return

        identifiers = []
        XMLDoc = minidom.parse(str(sys.argv[1])) #Get XML doc from system argument provided from UI

        #.pdf files
        try: 
            pdfPaths = XMLDoc.getElementsByTagName("pdfpath") #Get pdfpath element from XML file
            pdfFiles = []
            for path in pdfPaths:
                pdfFiles.append(path.firstChild.data) #Extract data from pdfpath element
        
            identifiers.extend(self.ParsePDF(pdfFiles))
        
        except:
            print("No .pdf files in directory or error related to .pdf")

        #.pcap files
        try:
            pcapPaths = XMLDoc.getElementsByTagName("pcappath")
            pcapFiles = []
            for path in pcapPaths:
                pcapFiles.append(path.firstChild.data)

            identifiers.extend(self.ParsePcap(pcapFiles))
        except:
            print("No .pcap files in directory or error related to .pcap")

        #.txt files
        #try:
        txtPaths = XMLDoc.getElementsByTagName("txtpath")
        txtFiles = []
        for path in txtPaths:
            txtFiles.append(path.firstChild.data)

        identifiers.extend(self.ParseTxt(txtFiles))
        #except:
        #    print("No .txt files in directory or error related to .txt")

        matchedIdentifiers = self.MatchIdentifiers(identifiers)
        self.CreateXMLDoc(matchedIdentifiers)

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
                ident = Identifier(ip, "IP-adresse", path, 0, id)
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
                ident = Identifier(ip, "IP", path, 0, id)
                identifiers.append(ident)
                id+=1
        
        return identifiers

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
                    ident = Identifier(number, "PhoneNumber", path, page, id)
                    identifiers.append(ident) #Add phone number identifiers to list
                    id +=1

                ips = regex.findIP(textDict[page]) #Find all IPv4 and IPv6 addresses using RegEx
                for ip in ips:
                    ident = Identifier(number, "IP", path, page, id)
                    identifiers.append(ident) #Add IP address identifiers to list
                    id +=1

        return identifiers

if __name__ == '__main__':
    mainClass = Main2()
    mainClass.main()
