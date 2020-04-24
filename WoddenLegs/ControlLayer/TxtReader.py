class TxtReader:
    
    def ReadFile(self, file):
        txt = open(file, "r")
        return txt.read()


