from xml.dom import minidom
import os

class XMLCreator:
    
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

            for path in identifier.paths: #Add list of paths the identifier is found in as child elements to the paths element.
                childOfPath = root.createElement('path')
                childOfPath.appendChild(root.createTextNode(path))
                childOfIdentifier.appendChild(childOfPath)

            childOfIdentifier = root.createElement('occurences') #Number of files the identifier was found in
            childOfIdentifier.appendChild(root.createTextNode(str(identifier.occurences)))
            identifierChild.appendChild(childOfIdentifier)

            childOfIdentifier = root.createElement('type') #Type of identifier
            childOfIdentifier.appendChild(root.createTextNode(identifier.type))
            identifierChild.appendChild(childOfIdentifier)

            childOfIdentifier = root.createElement('isBlacklisted') #This element is used by the UI to blacklist identifiers.
            childOfIdentifier.appendChild(root.createTextNode('False'))
            identifierChild.appendChild(childOfIdentifier)

        xml_str = root.toprettyxml(indent="\t") #Format XML

        currentDir = os.getcwd()
        save_path_file = currentDir + '\MatchedIdentifiers.xml' #Set document title + path
        with open(save_path_file, "w") as f: #Save XML doc
            f.write(xml_str)

