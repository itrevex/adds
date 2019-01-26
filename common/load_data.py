import json
import io
import os
import re

from .messages import Messages

class LoadData:
    def __init__(self):
        self.fileDir = os.path.dirname(__file__)
        self.head, self.tail = os.path.split(self.fileDir)
        if(self.tail != 'layers.json'): self.fileDir = self.head

    def getFile(self, file_path):
        return os.path.join(self.fileDir, file_path)

    def printData(self):
        print("file dir: " + self.fileDir)
        print("head: " + self.head)
        print("tail: " + self.tail)

    def getLayers(self):
        return self.loadJson("assests/layers.json")

    def getHeaderAttribs(self):
        return self.loadJson("assests/header_attribs.json")

    def getInputData(self):
        return self.loadJson("input/input_data.json")

    def loadJson(self, file_name):
        try:
            return json.load(io.open(self.getFile(file_name), encoding='utf8'))
        except json.decoder.JSONDecodeError as err:
         
            line = "in line "
            try:
                line += re.search('line (.+?) column', str(err)).group(1)
            except AttributeError:
                line = ""

            message = "File \"%s\" has an error %s "%(file_name, line)
            message += "\n\nMake sure there are no trailing commas after input and"
            message += "\nall text is in quotes."
            message += "\nCross check with sample input and make sure inputs are of a similar format"
            Messages.showError(message)

    