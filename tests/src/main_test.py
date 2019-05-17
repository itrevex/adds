# from beams.details.all_beams import AllBeams
from src.common.load_data import LoadData
from tests.snaps.input.layers import Layers

app_data = LoadData()
# all_beams = AllBeams(app_data);

def test_input():
    # print(app_data.getLayers());
    layers = Layers()
    assert app_data.getLayers() == layers.getLayerContent()