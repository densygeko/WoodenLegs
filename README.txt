How to:
1. Open Project4\WoddenLegs\WoddenLegs.sln with Visual Studio
2. Start GUI
3. Select the 3 dots icon in the top right corner and click insæt dokument
4. Select a directory to parse. (Use the TestingData folder that we provided you with)
5. System finds all phone numbers, emails, and ip-addresses in the directory
6. System checks if any of the identifiers were found in multiple files and shows them in the GUI

Be sure to check out the back-end python system at Project4\WoddenLegs\PythonBackend

*******************************************************************************************************
How to build a new backend .exe
Download pyinstaller with pip.
Run command 'pyinstaller --onefile ControlLayer\Main2.py' from WoddenLegs\PythonBackend
Pyinstaller cannot find class dependencies on its own, so you have to create new .spec files in the PythonBackend directory when you create new python classes.
Create .spec files with this command: 'pyi-makespec --paths=/path/to/thisdir \ --paths=/path/to/class file.py'

Python libraries:
re
csv
cv2
pytesseract
PIL
xml.dom
scapy.all
PyPDF4
numpy