import sys
sys.path.append("./detailing/")

from detailing import Detailing


if __name__ == "__main__":
    detailing = Detailing()
    detailing.makeDxf()