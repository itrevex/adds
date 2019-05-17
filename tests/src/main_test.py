# from beams.details.all_beams import AllBeams
from src.common.load_data import LoadData

app_data = LoadData()

def test_input(layerContent):
    assert app_data.getLayers() == layerContent