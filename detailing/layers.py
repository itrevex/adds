class Layers:

    def __init__(self, dwg):
        self.dwg = dwg
        self.addLayers()
        pass

    def addLayers(self):
        self.dwg.layers.new(name='MyLines', dxfattribs={'linetype': 'DASHED', 'color': 7})
        pass