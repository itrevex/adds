class Layers:
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