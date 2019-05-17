import pytest

from tests.snaps.input.layers import Layers


@pytest.fixture
def layerContent():
    return Layers().getLayerContent()
