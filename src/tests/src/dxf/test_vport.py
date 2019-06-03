from unittest.mock import patch, Mock
from src.dxf.vport import VPort

class TestVPort():
    def test_createVPortTable(self):
        dwg = Mock()
        dwg.viewports = Mock()
        dwg.viewports.new = Mock(side_effect = lambda name, attribs: None)
        VPort(dwg, 3)
        dwg.viewports.new.assert_called_once()
        attribs = {
            "height": 7000. * 3,
            "aspect_ratio": 1
        }
        dwg.viewports.new.assert_called_once_with("*active", attribs)
