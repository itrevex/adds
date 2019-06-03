import pytest
from tests.test_mocks.test_mocks_common.load_data_mocks import LoadDataMocks

@pytest.fixture
def LoadDataLayerContent():
    return LoadDataMocks().getLayerContent()

@pytest.fixture
def LoadDataHeaderAttribs():
    return LoadDataMocks().getHeaderAttribs()

@pytest.fixture
def LoadDataTextStyles():
    return LoadDataMocks().getTextStyles()

@pytest.fixture
def LoadDataLines():
    return [LoadDataMocks().lines(), LoadDataMocks().strippedLines()]


