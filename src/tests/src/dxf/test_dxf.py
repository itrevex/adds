import pytest
from unittest.mock import patch, Mock, PropertyMock
from src.dxf.vport import VPort
from src.dxf.dxf import DxfDraw
from src.common.messages import Messages
from src.dxf.dxf_entities.entity_line import EntityLine
from tests.mocks.dxf.dxf_mocks import DxfDrawMocks

@patch.object(DxfDraw, "addStylesToModelSpace")
@patch.object(DxfDraw, "setHeaderAttribs")
@patch.object(Messages, "continuePrompt")
class TestDxfDraw():

    def fake_appData(self):
        app_data = Mock()
        app_data.getOutPutFile = Mock(side_effect = lambda : "c:/fake/path.dxf")
        layers = {
            "layer1":{
                "layername": "FAKE-LAYER-1",
                "color": 1,
                "linetype": "Continuous" 
            }, 
            "layer2":{
                "layername": "FAKE-LAYER-2",
                "color": 3,
                "linetype": "Continuous" 
            }
        }

        app_data.getLayers = Mock(side_effect = lambda: layers)
        return app_data

    @patch.object(DxfDraw, "addLayersToModelSpace")
    @patch('src.dxf.dxf.ezdxf.new', side_effect=DxfDrawMocks.fake_dwg)
    def test_makeDxf(self, *arg):
        with patch.object(VPort, 'createVPortTable') as fake_VPort, \
            patch.object(DxfDraw, "drawEntities") as fake_drawEntities:
            app_data = self.fake_appData()
            DxfDraw(app_data).makeDxf({}, 2)
            fake_VPort.assert_called_once()
            fake_drawEntities.assert_called_once()
    
    @patch.object(DxfDraw, "addLayersToModelSpace")
    @patch('src.common.messages.sys.exit')
    @patch('src.dxf.dxf.ezdxf.new', side_effect=DxfDrawMocks.fake_dwg_raise)
    def test_makeDxfException(self, *arg):
        with patch.object(VPort, 'createVPortTable'), \
            patch.object(DxfDraw, "drawEntities"):
            app_data = self.fake_appData()
            assert DxfDraw(app_data).makeDxf({}, 2) == None

    @patch('src.common.utils.Utils.dateTimeString')
    def test_getFileName(self, fake_dateTimeString, *arg):
        fake_dateTimeString.return_value = "190529_1536"
        app_data = self.fake_appData()
        assert DxfDraw(app_data).getFileName() == "190529_1536-detail.dxf"

    @patch.object(DxfDraw, 'getLayer')
    @patch('src.dxf.dxf.ezdxf.new')
    def test_addDxfLine(self, fake_dwg, fake_getLayer, *arg):
        pt1 = (0.,0.,0.)
        pt2 = (20.,0.,3)

        line = EntityLine(pt1, pt2, "fake_layer")
        fake_msp = Mock()
        type(fake_dwg.return_value).modelspace = fake_msp
        fake_add_line = Mock()
        type(fake_msp.return_value).add_line = fake_add_line

        app_data = self.fake_appData()
        DxfDraw(app_data).addDxfLine(line)
        fake_dwg.assert_called_once()
        fake_getLayer.assert_called_once()
        fake_msp.assert_called_once()
        fake_add_line.assert_called_once()


    @patch.object(DxfDraw, 'getLayer')
    @patch('src.dxf.dxf.ezdxf.new')
    def test_addCircle(self, fake_dwg, fake_getLayer, *arg):
    
        app_data = self.fake_appData()
        fake_msp = Mock()
        type(fake_dwg.return_value).modelspace = fake_msp
        fake_add_circle = Mock()
        type(fake_msp.return_value).add_circle = fake_add_circle

        DxfDraw(app_data).addDxfCircle(Mock())
        fake_dwg.assert_called_once()
        fake_getLayer.assert_called_once()
        fake_msp.assert_called_once()
        fake_add_circle.assert_called_once()


    @patch.object(DxfDraw, 'getLayer')
    @patch('src.dxf.dxf.ezdxf.new')
    def test_addDxfText(self, fake_dwg, fake_getLayer, *arg):
    
        app_data = self.fake_appData()
        fake_msp = Mock()
        type(fake_dwg.return_value).modelspace = fake_msp
        fake_add_text = Mock()
        type(fake_msp.return_value).add_text = fake_add_text

        DxfDraw(app_data).addDxfText(Mock())
        fake_dwg.assert_called_once()
        fake_getLayer.assert_called_once()

        fake_msp.assert_called_once()
        fake_add_text.assert_called_once()
        

        pass

    @patch.object(DxfDraw, 'getLayerColor')
    @patch.object(DxfDraw, 'getLayer')
    @patch('src.dxf.dxf.ezdxf.new')
    def test_addDxfHatch(self, fake_dwg, fake_getLayer, fake_getLayerColor, *arg):
    
        app_data = self.fake_appData()

        fake_msp = Mock()
        type(fake_dwg.return_value).modelspace = fake_msp
        fake_add_hatch = Mock()
        type(fake_msp.return_value).add_hatch = fake_add_hatch
        fake_edit_boundary = Mock()
        type(fake_add_hatch.return_value).edit_boundary = fake_edit_boundary
        fake_add_polyline_path = Mock()
        fake_enter = Mock(side_effect=lambda:fake_add_polyline_path)
        fake_exit = Mock()
        type(fake_edit_boundary.return_value).add_polyline_path = fake_add_polyline_path
        type(fake_edit_boundary.return_value).__enter__ = fake_enter
        type(fake_edit_boundary.return_value).__exit__ = fake_exit


        DxfDraw(app_data).addDxfHatch(Mock())
        fake_dwg.assert_called_once()
        fake_getLayer.assert_called_once() 
        fake_getLayerColor.assert_called_once() 

        fake_msp.assert_called_once()
        fake_add_hatch.assert_called_once()
        fake_edit_boundary.assert_called_once()
        fake_enter.assert_called_once()
        fake_exit.assert_called_once()
        
        # fake_add_polyline_path.assert_called_once()

        pass
                

    @patch('src.dxf.dxf.ezdxf.new')
    def test_getLayer(self, fake_dwg, *arg):
    
        app_data = self.fake_appData()
        assert DxfDraw(app_data).getLayer('layer1') == "FAKE-LAYER-1"
        assert DxfDraw(app_data).getLayer() == '0'

        pass

    @patch('src.dxf.dxf.ezdxf.new')
    def test_getLayerColor(self, fake_dwg, *arg):
    
        app_data = self.fake_appData()
        assert DxfDraw(app_data).getLayerColor('layer1') == 1
        assert DxfDraw(app_data).getLayerColor() == '7'

        pass
    @patch('src.dxf.dxf.SHOW_DIMENSION', autospec=True)
    def test_addDxfEntity(self, fake_show_dimension):
        app_data = self.fake_appData()
        DxfDraw(app_data).addDimEntity(Mock())
        pass


