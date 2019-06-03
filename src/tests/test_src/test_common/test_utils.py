from unittest.mock import patch, PropertyMock, Mock
import datetime
from common.utils import Utils
from tests.test_mocks.test_mocks_common.utils_mocks import UtilsMocks
from freezegun import freeze_time

class TestUtils():

    def test_dateString(self):
        with patch.object(Utils, 'getNow') as fake_getNow:
            fake_getNow.return_value = datetime.datetime(2018, 3, 4, 5, 35)
            # assert Utils.dateString() == "180304"

    def test_getNow(self):
        assert Utils.getNow() != datetime.datetime(2012, 1, 14)
        with freeze_time("2012-01-14"):
            assert Utils.getNow() == datetime.datetime(2012, 1, 14)
            
            

    def test_timeString(self):
        with patch.object(Utils, 'getNow') as fake_getNow:
            fake_getNow.return_value = datetime.datetime(2018, 3, 4, 5, 35)
            assert Utils.timeString() == "0535"

    def test_dateTimeString(self):
        with patch.object(Utils, 'getNow') as fake_getNow:
            fake_getNow.return_value = datetime.datetime(2018, 3, 4, 5, 35)
            assert Utils.dateTimeString() == "180304_0535" 