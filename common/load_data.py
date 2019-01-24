import json
import io
import os

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
        return json.load(io.open(self.getFile("assests/layers.json"), encoding='utf8'))

    def getHeaderAttribs(self):
        return json.load(io.open(self.getFile("assests/header_attribs.json"), encoding='utf8'))

    def getInputData(self):
        return json.load(io.open(self.getFile("assests/input_data.json"), encoding='utf8'))



    