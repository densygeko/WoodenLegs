import csv


class CsvReader: #Reads .csv files and returns the content as rows

    def ReadFile(self, file):
        csvRows = []
        with open(file, 'r') as csvFile: #Open file
            reader = csv.reader(csvFile, delimiter = '\t') #Reader iterates over the .csv file's rows
            for row in reader:
                csvRows.append(row) #Add each row to list

        return csvRows