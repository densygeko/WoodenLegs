from ModelLayer.Identifier import *
from ModelLayer.MatchedIdentifier import *
from ControlLayer.FileParser import *
from ControlLayer.XMLCreator import *
from xml.dom import minidom
import sys
import os
import ast

class Main2():

    def main(self): #Needs to be updated to take a list of lists of paths
        if len(sys.argv) <= 1: #Must have at least one argument when executing this class in command line
            print("Please enter the path to the filepaths.xml document")
            return
        
        xmlCreator = XMLCreator()
        identifiers = self.SortFiles(sys.argv[1]) #Extract identifiers from text
        matchedIdentifiers = self.MatchIdentifiers(identifiers) #Match duplicate identifiers
        xmlCreator.CreateXMLDoc(matchedIdentifiers) #Create XML doc with matched identifiers data

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

    #Sort files into the right Parsers.
    def SortFiles(self, xmlPath):
        identifiers = []
        print(str(xmlPath))
        XMLDoc = minidom.parse(str(xmlPath)) #Get XML doc from system argument provided from UI
        fileParser = FileParser()

        #.pdf files
        try: 
            pdfPaths = XMLDoc.getElementsByTagName("pdfpath") #Get pdfpath element from XML file
            pdfFiles = []
            for path in pdfPaths:
                pdfFiles.append(path.firstChild.data) #Extract data from pdfpath element
        
            identifiers.extend(fileParser.ParsePDF(pdfFiles))
        
        except:
            print("No .pdf files in directory or error related to .pdf")

        #.pcap files
        try:
            pcapPaths = XMLDoc.getElementsByTagName("pcappath")
            pcapFiles = []
            for path in pcapPaths:
                pcapFiles.append(path.firstChild.data)

            identifiers.extend(fileParser.ParsePcap(pcapFiles))
        except:
            print("No .pcap files in directory or error related to .pcap")

        #.txt files
        try:
            txtPaths = XMLDoc.getElementsByTagName("txtpath")
            txtFiles = []
            for path in txtPaths:
                txtFiles.append(path.firstChild.data)

            identifiers.extend(fileParser.ParseTxt(txtFiles))
        except:
            print("No .txt files in directory or error related to .txt")

        #.csv files
        try:
            csvPaths = XMLDoc.getElementsByTagName("csvpath")
            csvFiles = []
            for path in csvPaths:
                csvFiles.append(path.firstChild.data)

            identifiers.extend(fileParser.ParseCsv(csvFiles))
        except:
            print("No .csv files in directory or error related to .csv")

        #Images
        try:
            imgPaths = XMLDoc.getElementsByTagName("imgpath")
            imgFiles = []
            for path in imgPaths:
                imgFiles.append(path.firstChild.data)

            identifiers.extend(fileParser.ParseImg(imgFiles))
        except:
            print("No images found in directory or error related to images")

        return identifiers

if __name__ == '__main__':
    mainClass = Main2()
    mainClass.main()