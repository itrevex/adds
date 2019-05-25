class LoadDataSnaps:
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

