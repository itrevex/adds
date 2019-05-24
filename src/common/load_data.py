import json
import io
import os
import re
import sys

from .messages import Messages
from .message_codes import MessageCodes

class LoadData:
    def __init__(self):
        self.fileDir = os.path.dirname(__file__)
        self.head, self.tail = os.path.split(self.fileDir)
        if(self.tail != 'layers.json'): self.fileDir = self.head
    
    def removeComments(self, lines):
        # Messages.d(line)
        lines_stripped = []
        for line in lines:
            if line != "" and re.search('^[*]', line) == None:
                lines_stripped.append(line)
        return lines_stripped

    def readTradFile(self):
        self.path = self.getInputFilePath()
        with open(self.getFile(self.path)) as f:
            lines = [line.strip() for line in f.readlines()]
            
        return self.removeComments(lines)            


    def getFile(self, file_path):
        return os.path.join(self.fileDir, file_path)

    def printData(self):
        print("file dir: " + self.fileDir)
        print("head: " + self.head)
        print("tail: " + self.tail)

    def getLayers(self):
        return self.loadJson("assests/layers.json")

    def getTextStyles(self):
        return self.loadJson("assests/text_styles.json")
        
    def getHeaderAttribs(self):
        return self.loadJson("assests/header_attribs.json")

    def getInputData(self):
        self.path = self.getInputFilePath()
        if (self.path == ""):
            return Messages.showError(MessageCodes.ERROR_WRONG_FILE_PATH)
        return self.loadJson(self.path)

    def loadJson(self, file_name):
        try:
            return json.load(io.open(self.getFile(file_name), encoding='utf8'))
        except json.decoder.JSONDecodeError as err:
         
            line = ""
            try:
                line += re.search('line (.+?) column', str(err)).group(1)
            except AttributeError:
                line = ""
            finally:
                # message = "File \"%s\" has an error %s "%(file_name, line)
                # message += "\n\nMake sure there are no trailing commas after input and"
                # message += "\nall text is in quotes."
                # message += "\nCross check with sample input and make sure inputs are of a similar format"
                error = MessageCodes.ERROR_INPUT_DATA_FORMAT
                error.setMsg(error.msg%(file_name, line))

                Messages.showError(error)

    def getInputFilePath(self):
        # if called with no arguments, call app data pick file from there
        path = ""
        if (len(sys.argv) > 1):
            path = self.getFile(sys.argv[1])
            
        else:
            path = self.getFile(os.getenv('LOCALAPPDATA') + "\\Trevexs Adds\\data\\sample1.trad")
        
        return path

    def getOutPutFile(self):
        try: 
            head, tail = os.path.split(self.path)
            file_name = tail.split('.')[0] + ".dxf"
            return os.path.join(head, file_name)

        except AttributeError as e:
            print(e)
            Messages.showError(MessageCodes.ERROR_NO_INPUT_DATA)