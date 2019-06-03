import json

class LoadDataMocks:
    def getLayerContent(self):
        return { 'CenterLines': {'layername': 'S-CENTRE', 'color': 1, 'linetype': 'CENTER'}, 
            'BeamLines': {'layername': 'S-CONCRETE', 'color': 150, 'linetype': 'Continuous'}, 
            'Zigzag': {'layername': 'S-18', 'color':1, 'linetype': 'Continuous'}, 
            'GridLines': {'layername': 'S-GRID', 'color': 1, 'linetype': 'CENTER'}, 
            'SupportLines': {'layername': 'S-CONCRETE', 'color': 1, 'linetype': 'CENTER'}, 
            'GridLabels': {'layername': 'S-GRID', 'color': 1, 'linetype': 'CENTER'}, 
            'BeamHatches': {'layername': 'S-FILL', 'color': 252, 'linetype': 'Continuous'}, 
            'SectionLines': {'layername': 'S-CONCRETE', 'color': 1, 'linetype': 'CENTER'}, 
            'Dimensions': {'layername': 'S-DIM-FAKE', 'color': 1, 'linetype': 'Continuous'}, 
            'ShearLinks': {'layername': 'S-35', 'color': 3, 'linetype': 'Continuous'}}

    def lines(self):
        return [
            '',
            'The boy is going to school'
        ]

    def strippedLines(self):
        return [
            'The boy is going to school'
        ]

    def getHeaderAttribs(self):
        return {'ltscale': {'attrib_name': '$LTSCALE', 'attrib_value': 18.0}, 
        'upper_right': {'attrib_name': '$EXTMAX', 'attrib_value': [10500, 1600, 0]}, 
        'lower_right': {'attrib_name': '$EXTMIN', 'attrib_value': [-600, -1800, 0]}}

    def getTextStyles(self):
        return {
            '175': {}, 
            'GridLabels': {'font': 'romans.ttf', 'height': 111.25, 'oblique': 0, 'width': 1}}


    @staticmethod
    def fake_getFile(self, fake_path="fake_path"):
        return fake_path

    @staticmethod
    def fake_loadJson(self, file_name):
        return "json_loaded: " + file_name

    @staticmethod
    def fake_loadJsonException(self, encoding=None):
        raise json.decoder.JSONDecodeError("An error occured", "me", 4)

    @staticmethod
    def fake_jsonIoOpen(self, encoding):
        return '{ "name":"John", "age":30, "city":"New York"}'

    @staticmethod
    def fake_getInputFilePath(self):
        return 'fake input path'

    @staticmethod
    def fake_setMsg(self, msg=""):
        return 'fake msg'

    @staticmethod
    def fake_os_path_split(self, path="fake/path"):
        return "head/path", "tail.ext"


