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

            childOfIdentifier = root.createElement('isBlacklisted')
            childOfIdentifier.appendChild(root.createTextNode('false'))
            identifierChild.appendChild(childOfIdentifier)

        xml_str = root.toprettyxml(indent="\t") #Format XML
        print("Pretty XMl string " + xml_str)
        print("Normal XML string " + root.toxml())

        currentDir = os.getcwd()
        save_path_file = currentDir + '\MatchedIdentifiers.xml' #Set document title + path
        with open(save_path_file, "w") as f: #Save XML doc
            f.write(xml_str)

