import json

class JsonFil:

    def __init__(self , file):

        self.Namefile = file

    def Read(self):

        self.Usefile = open(self.Namefile)

        file = json.load(self.Usefile)

        for i in file:

            print(i)

        self.Usefile.close()



file = JsonFil("Account.json")
file.Read()
