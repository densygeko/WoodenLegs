from ControlLayer.PDFReader import *
from ControlLayer.RegexChecker import *
from ModelLayer.Identifier import *
from ModelLayer.MatchedIdentifier import *
import sys
import os
from xml.dom import minidom

class Main2():

    def MatchIdentifiers(self, identifiers):
        matchedIdentifiers = []
        for i in identifiers: #Loop through each identifier.
            if i.isMatched == False: #Don't check the identifier if it has already been matched.
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

            childOfIdentifier = root.createElement('path')
            childOfIdentifier.appendChild(root.createTextNode(identifier.path))
            identifierChild.appendChild(childOfIdentifier)

            childOfIdentifier = root.createElement('page')
            childOfIdentifier.appendChild(root.createTextNode(str(identifier.page)))
            identifierChild.appendChild(childOfIdentifier)

            childOfIdentifier = root.createElement('type')
            childOfIdentifier.appendChild(root.createTextNode(identifier.type))
            identifierChild.appendChild(childOfIdentifier)

        xml_str = root.toprettyxml(indent="\t") #Format XML

        save_path_file = "text.xml" #Set document title
        with open(save_path_file, "w") as f: #Save XML doc
            f.write(xml_str)

    def main(self): #Needs to be updated to take a list of lists of paths
        paths = ['ControlLayer\\TempPDFHolder\\TestPDF.pdf', 'ControlLayer\\TempPDFHolder\\TestPDF2.pdf']

        for arg in sys.argv[1:]: #Needs to be finished so that it can take system args
            print(arg)

        id = 0 #Id gets incremented when searching for identifiers and attached to them
        identifiers = []
        for path in paths:
            textDict = PdfReader.readImages(path) #Gets all normal text and text on images from PDF
            for page in textDict:
                
                emails = RegexChecker.checkMail(textDict[page]) #Add email identifiers to list
                for email in emails:
                    ident = Identifier(email, "Email", path, page, id)
                    identifiers.append(ident)
                    id +=1
                
                phoneNumbers = RegexChecker.checkPhone(textDict[page]) #Add phone number identifiers to list
                for number in phoneNumbers:
                    ident = Identifier(number, "PhoneNumber", path, page, id)
                    identifiers.append(ident)
                    id +=1

                ips = RegexChecker.findIP(textDict[page]) #Add IP address identifiers to list
                for ip in ips:
                    ident = Identifier(number, "IP", path, page, id)
                    identifiers.append(ident)
                    id +=1

        self.MatchIdentifiers(identifiers) #Sort identifiers and get the ones with multiple occurences.
        self.CreateXMLDoc(identifiers) 

if __name__ == '__main__':
    mainClass = Main2()
    mainClass.main()
