# from beams.details.all_beams import AllBeams
from src.common.load_data import LoadData

class TestLoadData:

    def test_input(self, LoadDataLayerContent):
        assert LoadData().getLayers() == LoadDataLayerContent

    def test_removeComments(self, LoadDataLines):
        lines_stripped = LoadData().removeComments(LoadDataLines[0])
        assert lines_stripped == LoadDataLines[1]



