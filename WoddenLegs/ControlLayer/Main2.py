from ModelLayer.Identifier import *
from ModelLayer.MatchedIdentifier import *
from ControlLayer.FileParser import *
from ControlLayer.XMLCreator import *
from xml.dom import minidom
import sys
import os
import ast
from threading import Thread

class Main2():

    def __init__(self):
        self.identifiers = []
        self.matchedIdentifiers = []

    def main(self): #Needs to be updated to take a list of lists of paths
        if len(sys.argv) <= 1: #Must have at least one argument when executing this class in command line
            print("Please enter the path to the filepaths.xml document")
            return
        
        XMLDoc = minidom.parse(str(sys.argv[1])) #Get XML doc from system argument provided from UI

        #Create one thread for each file type in XML doc.
        pdfThread = Thread(target=self.PdfThread, args=(XMLDoc.getElementsByTagName("pdfpath"),))     #The comma is added to the argument is seen as a tuple.
        pcapThread = Thread(target=self.PcapThread, args=(XMLDoc.getElementsByTagName("pcappath"),))  #When a thread takes a list as an argument, it attempts
        csvThread = Thread(target=self.CsvThread, args=(XMLDoc.getElementsByTagName("csvpath"),))     #to split the argument into multiple bits.
        imgThread = Thread(target=self.ImgThread, args=(XMLDoc.getElementsByTagName("imgpath"),))
        txtThread = Thread(target=self.TxtThread, args=(XMLDoc.getElementsByTagName("txtpath"),))

        #Start Threads
        pdfThread.start()
        pcapThread.start()
        csvThread.start()
        imgThread.start()
        txtThread.start()


        #Wait for threads to finish
        pdfThread.join()
        pcapThread.join()
        csvThread.join()
        imgThread.join()
        txtThread.join()

        #Seperate identifiers into lists by type
        emailIdentifiers = []
        phoneIdentifiers = []
        ipIdentifiers = []
        print(str(len(self.identifiers)))
        for i in self.identifiers:
            if i.type == "Email":
                emailIdentifiers.append(i)
            elif i.type == "Telefon Nr.":
                phoneIdentifiers.append(i)
            elif i.type == "IP-adresse":
                ipIdentifiers.append(i)

        #Create threads to match identifiers
        emailThread = Thread(target=self.MatchIdentifiers, args=(emailIdentifiers,))
        phoneThread = Thread(target=self.MatchIdentifiers, args=(phoneIdentifiers,))
        ipThread = Thread(target=self.MatchIdentifiers, args=(ipIdentifiers,))

        #Start threads
        emailThread.start()
        phoneThread.start()
        ipThread.start()

        #Wait for threads to finish
        emailThread.join()
        phoneThread.join()
        ipThread.join()

        xmlCreator = XMLCreator()
        xmlCreator.CreateXMLDoc(self.matchedIdentifiers) #Create XML doc with matched identifiers data

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
                            print(i.name + " and " + j.name + " have been matched \n")
                            paths.append(j.path)
                            if match == None: #Create MatchedIdentifier at first occurence of a matching identifier
                                match = MatchedIdentifier(i.name, i.type, paths, i.id, 1)
                                print("A new MatchedIdentifier object was created for " + i.name + "\n")
                            else:
                                match.paths = paths
                                print("A MatchedIdentifier object already exists for " + j.name + " Adding path to list of paths. \n")
                            
                            match.occurences +=1 #At all following occurences of the same identifier, increment occurences
                            j.isMatched = True #The method won't loop through objects that have already been matched

                if match != None: #Only add match object to list if it has been instantiated
                    matchedIdentifiers.append(match)
                    i.isMatched = True

        self.matchedIdentifiers.extend(matchedIdentifiers)
            
    def PdfThread(self, pdfPaths):
        #.pdf files
        fileParser = FileParser()
        try: 
            pdfFiles = []
            for path in pdfPaths:
                pdfFiles.append(path.firstChild.data) #Extract data from pdfpath element
        
            self.identifiers.extend(fileParser.ParsePDF(pdfFiles))
        
        except:
            print("No .pdf files in directory or error related to .pdf")

    def PcapThread(self, pcapPaths):
        #.pcap files
        fileParser = FileParser()
        try:
            pcapFiles = []
            for path in pcapPaths:
                pcapFiles.append(path.firstChild.data)

            self.identifiers.extend(fileParser.ParsePcap(pcapFiles))
        except:
            print("No .pcap files in directory or error related to .pcap")

    def TxtThread(self, txtPaths):
        #.txt files
        fileParser = FileParser()
        try:
            txtFiles = []
            for path in txtPaths:
                txtFiles.append(path.firstChild.data)

            self.identifiers.extend(fileParser.ParseTxt(txtFiles))
        except:
            print("No .txt files in directory or error related to .txt")

    def CsvThread(self, csvPaths):
        #.csv files
        fileParser = FileParser()
        
        csvFiles = []
        for path in csvPaths:
            csvFiles.append(path.firstChild.data)

        self.identifiers.extend(fileParser.ParseCsv(csvFiles))
        #except:
        #    print("No .csv files in directory or error related to .csv")

    def ImgThread(self, imgPaths):
        #Images
        fileParser = FileParser()
        try:
            imgFiles = []
            for path in imgPaths:
                imgFiles.append(path.firstChild.data)

            self.identifiers.extend(fileParser.ParseImg(imgFiles))
        except:
            print("No images found in directory or error related to images")

if __name__ == '__main__':
    mainClass = Main2()
    mainClass.main()