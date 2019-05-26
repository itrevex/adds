from src.common.constants import Constants

class TestConstants():
    def test_constants(self):
        constants = Constants()
        assert constants.CURRENT_BUILD == 1002