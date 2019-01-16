import sys
sys.path.append("./detailing/")
sys.path.append("./common/")

from detailing import Detailing
from load_data import LoadData

appData = LoadData()

if __name__ == "__main__":
    detailing = Detailing(appData)
    detailing.trials()
    # detailing.availableLineTypes()
    