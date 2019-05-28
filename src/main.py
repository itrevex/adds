from src.beams.details.all_beams import AllBeams
from src.dxf.dxf import DxfDraw
from src.common.load_data import LoadData
from src.common.messages import Messages
# import beams.dimensions.trial_dim 

app_data = LoadData()

if __name__ == "__main__":
    # appData.getInputFilePath()
    Messages.i("")
    all_beams = AllBeams(app_data)
    dxfDraw = DxfDraw(app_data)
    dxfDraw.makeDxf(all_beams.getAllBeamsEntities(), all_beams.number_of_beams)
    
    try:
        pass
    except:
        print("There is an unknown error in the program, contact developers")
    # beams.availableLineTypes()
    pass