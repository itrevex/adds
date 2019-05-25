import pytest
from tests.snaps.common.load_data_snaps import LoadDataSnaps

@pytest.fixture
def LoadDataLayerContent():
    return LoadDataSnaps().getLayerContent()

@pytest.fixture
def LoadDataHeaderAttribs():
    return LoadDataSnaps().getHeaderAttribs()

@pytest.fixture
def LoadDataTextStyles():
    return LoadDataSnaps().getTextStyles()

@pytest.fixture
def LoadDataLines():
    return [LoadDataSnaps().lines(), LoadDataSnaps().strippedLines()]


