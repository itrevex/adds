
from detailing.detailing import Detailing
from detailing.details import AllBeamsDetails
from detailing.dxf import DxfDraw
from common.load_data import LoadData

app_data = LoadData()

if __name__ == "__main__":
    # appData.getInputFilePath()
    all_beams = AllBeamsDetails(app_data);
    dxfDraw = DxfDraw(app_data)
    dxfDraw.drawEntities(all_beams.getAllBeamsEntities())
    dxfDraw.makeDxf()
    # detailing.availableLineTypes()
    