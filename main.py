
from detailing.detailing import Detailing
from common.load_data import LoadData

appData = LoadData()

if __name__ == "__main__":
    detailing = Detailing(appData)
    detailing.trials()
    # detailing.availableLineTypes()
    