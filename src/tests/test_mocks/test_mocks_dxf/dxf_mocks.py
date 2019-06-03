from unittest.mock import patch, Mock, PropertyMock

class DxfDrawMocks():

    @staticmethod
    def fake_dwg(self):
        dwg = Mock()
        modelspace = PropertyMock(side_effect=lambda : Mock())
        type(dwg.return_value).modelspace = modelspace
        add_line = PropertyMock(side_effect=lambda *arg, **kw: "line added")
        type(modelspace).add_line = add_line
        # msp.add_line = Mock(side_effect=lambda *arg, **kw: "line added")
        return dwg

    @staticmethod
    def fake_msp(self):
        msp = DxfDrawMocks.fake_dwg.modelspace()
        msp.add_line = Mock(side_effect=lambda *arg, **kw: "line added")
        return msp

    @staticmethod
    def fake_dwg_raise(self):
        dwg = Mock()
        dwg.modelspace = Mock(side_effect=lambda : "fake model space")
        dwg.saveas = Mock(side_effect = lambda *arg : exec('raise(PermissionError(*arg))'))
        return dwg

    @staticmethod
    def fake_getLayer(self, layer=None):
        return layer
