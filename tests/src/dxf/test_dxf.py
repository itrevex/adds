import pytest
from unittest.mock import patch, Mock
from src.dxf.vport import VPort
from src.dxf.dxf import DxfDraw
from src.common.messages import Messages
from tests.mocks.dxf.dxf_mocks import DxfDrawMocks

class TestDxfDraw():

    def fake_appData(self):
        app_data = Mock()
        app_data.getOutPutFile = Mock(side_effect = lambda : "c:/fake/path.dxf")
        return app_data

    @patch.object(DxfDraw, "addLayersToModelSpace")
    @patch.object(DxfDraw, "addStylesToModelSpace")
    @patch.object(DxfDraw, "setHeaderAttribs")
    @patch.object(Messages, "continuePrompt")
    @patch('src.dxf.dxf.ezdxf.new', side_effect=DxfDrawMocks.fake_dwg)
    def test_makeDxf(self, *arg):
        with patch.object(VPort, 'createVPortTable') as fake_VPort, \
            patch.object(DxfDraw, "drawEntities") as fake_drawEntities:
            app_data = self.fake_appData()
            DxfDraw(app_data).makeDxf({}, 2)
            fake_VPort.assert_called_once()
            fake_drawEntities.assert_called_once()

    @patch.object(DxfDraw, "addLayersToModelSpace")
    @patch.object(DxfDraw, "addStylesToModelSpace")
    @patch.object(DxfDraw, "setHeaderAttribs")
    @patch.object(Messages, "continuePrompt")
    @patch('src.common.messages.sys.exit')
    @patch('src.dxf.dxf.ezdxf.new', side_effect=DxfDrawMocks.fake_dwg_raise)
    def test_makeDxfException(self, *arg):
        with patch.object(VPort, 'createVPortTable'), \
            patch.object(DxfDraw, "drawEntities"):
            app_data = self.fake_appData()
            assert DxfDraw(app_data).makeDxf({}, 2) == None
                



