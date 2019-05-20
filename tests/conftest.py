import pytest
from tests.snaps.common.load_data_snaps import LoadDataSnaps

@pytest.fixture
def LoadDataLayerContent():
    return LoadDataSnaps().getLayerContent()

@pytest.fixture
def LoadDataLines():
    return [LoadDataSnaps().lines(), LoadDataSnaps().strippedLines()]


