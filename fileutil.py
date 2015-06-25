import json

from properties import filename

class FileManager():
    def __init__(self):
        self.filename = filename
        self.load_file(self.filename)
        self.schema()
  
    def load_file(self, filename):
        try:
            with open(filename) as data:
                self.data = json.load(data)
        except IOError:
            self.data = {}
    
    def schema(self):
        self.data.setdefault('scores':{})
    
    def save_file(self, filename):
        with open(self.filename, 'w') as outfile:
            json.dump(self.data, outfile)


 

