class VPort:
    '''
    Creates drawing vport to zoom drawing to the extents
    '''
    def __init__(self, dwg, number_of_beams):
        self.dwg = dwg
        self.createVPortTable(number_of_beams)
        pass

    def createVPortTable(self, number_of_beams):
        attributes = {
            # "snap_base": (-600, -1800),
            # "upper_right": (10500, 1600),
            "height": 7000. * number_of_beams,
            "aspect_ratio": 1
        }
        self.dwg.viewports.new("*active", attributes)