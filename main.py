from detailing.details.all_beams import AllBeamsDetails
from detailing.dxf import DxfDraw
from common.load_data import LoadData
from common.messages import Messages
# import detailing.dimensions.trial_dim 

app_data = LoadData()

if __name__ == "__main__":
    # appData.getInputFilePath()
    Messages.i("")
    all_beams = AllBeamsDetails(app_data)
    dxfDraw = DxfDraw(app_data)
    dxfDraw.drawEntities(all_beams.getAllBeamsEntities())
    dxfDraw.makeDxf()
    
    try:
        pass
    except:
        print("There is an unknown error in the program, contact developers")
    # detailing.availableLineTypes()
    pass