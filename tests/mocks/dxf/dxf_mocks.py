from unittest.mock import patch, Mock

class DxfDrawMocks():

    @staticmethod
    def fake_dwg(self):
        dwg = Mock()
        dwg.modelspace = Mock(side_effect=lambda : "fake model space")
        return dwg

    def fake_dwg_raise(self):
        dwg = Mock()
        dwg.modelspace = Mock(side_effect=lambda : "fake model space")
        dwg.saveas = Mock(side_effect = lambda *arg : exec('raise(PermissionError(*arg))'))
        return dwg
