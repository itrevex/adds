# from beams.details.all_beams import AllBeams
from src.common.load_data import LoadData
from src.common.messages import Messages
from src.common.message_codes import MessageCode, MessageCodes
import pytest, io, sys, json
import unittest.mock as mock
from json.decoder import JSONDecodeError

class FakeLoadData:
    @staticmethod
    def fake_getFile(self, fake_path="fake_path"):
        return fake_path

    @staticmethod
    def fake_loadJson(self, file_name):
        return "json_loaded: " + file_name

    @staticmethod
    def fake_loadJsonException(self, encoding=None):
        raise json.decoder.JSONDecodeError("An error occured", "me", 4)

    @staticmethod
    def fake_loadJsonAttributeException(self, encoding=None):
        raise AttributeError("Wrong attribute error test")

    @staticmethod
    def fake_jsonIoOpen(self, encoding):
        return '{ "name":"John", "age":30, "city":"New York"}'

    @staticmethod
    def fake_getInputFilePath(self):
        return 'fake input path'

    @staticmethod
    def fake_getMsg(self, msg=""):
        return 'fake msg'

class TestLoadData:

    def test_input(self, LoadDataLayerContent):
        assert LoadData().getLayers() == LoadDataLayerContent

    def test_removeComments(self, LoadDataLines):
        lines_stripped = LoadData().removeComments(LoadDataLines[0])
        assert lines_stripped == LoadDataLines[1]

    @mock.patch.object(LoadData, 'getFile', FakeLoadData.fake_getFile)
    def test_getFile(self):
        assert LoadData().getFile("fake_path") == 'fake_path'

    @mock.patch.object(LoadData, 'loadJson', FakeLoadData.fake_loadJson)
    @mock.patch('src.common.load_data.json.load')
    @mock.patch('src.common.load_data.io.open')
    def test_loadJson(self, fake_json_load, fake_io_open):
        fake_json_load.return_value = "json_loaded"
        fake_io_open.return_value = 'file_opened'
        assert LoadData().loadJson('fake path') == 'json_loaded: fake path'

    @mock.patch('src.common.load_data.json.load')
    @mock.patch('src.common.load_data.io.open')
    @mock.patch('src.common.load_data.sys.exit')
    def test_LoadJson_exception(self, fake_json_load, 
        fake_io_open,fake_sys_exit):
        fake_json_load.return_value = "json_loaded"
        fake_io_open.side_effect = FakeLoadData.fake_loadJsonException
        fake_sys_exit.side_effect = FakeLoadData.fake_loadJsonException
        assert LoadData().loadJson('fake path') is None
    
    def test_loadJson_attribute_exception(self):
        
        with mock.patch('src.common.load_data.json.load') as fake_json_load, \
            mock.patch('src.common.load_data.re.search', FakeLoadData.fake_loadJsonAttributeException), \
            mock.patch.object(MessageCode, 'setMsg') as fake_setMsg, \
            mock.patch.object(MessageCodes, 'ERROR_INPUT_DATA_FORMAT') as fake_MessageCode, \
            mock.patch('src.common.load_data.sys.exit') as fake_sys_exit, \
            mock.patch('src.common.load_data.io.open') as fake_io_open:
            fake_io_open.return_value = "file opened"
            fake_sys_exit.return_value = "System exit"
            fake_setMsg.side_effect = FakeLoadData.fake_getMsg
            # type(fake_MessageCode.return_value).msg = mock.PropertyMock(return_value="fake error msg")
            fake_json_load.side_effect = FakeLoadData.fake_loadJsonException
            assert LoadData().loadJson('fake path') is None
               
    @mock.patch.object(LoadData, 'loadJson', FakeLoadData.fake_loadJsonException)
    def test_LoadJsonException(self):
        # loadJson.side_effect = Exception()
        with pytest.raises(JSONDecodeError) as error:
            assert LoadData().loadJson('{"me":"me"}')
        assert str(error.value) == 'An error occured: line 1 column 5 (char 4)'
    
    @mock.patch.object(LoadData, 'loadJson', FakeLoadData.fake_loadJsonException)
    @mock.patch('src.common.messages.sys.exit')
    def test_LoadJsonExceptionLogic(self,fake_sys_exit):
        try:
            LoadData().loadJson('input_file')
        except JSONDecodeError:
            pass

    @mock.patch.object(LoadData, 'getFile')
    @mock.patch.object(sys, 'argv')
    def test_getInputFilePath(self, fake_getFile, fake_sys_argv):
        fake_getFile.side_effect = FakeLoadData.fake_getFile
        fake_sys_argv.return_value = None
        assert LoadData().getInputFilePath() == None

    # @mock.patch.object(LoadData, 'getFile')
    @mock.patch.object(sys, 'argv', ["d", "e"])
    def test_getInputFilePathElse(self):
        with mock.patch.object(LoadData, 'getFile', FakeLoadData.fake_getFile):
            assert LoadData().getInputFilePath() == 'e'

    @mock.patch('src.common.load_data.sys.exit')
    @mock.patch.object(Messages, 'showError')
    def test_getInputData(self, fake_sys_exit, fake_showError):
        '''
        Test get input data method calls
        '''

        fake_sys_exit.return_value = "system exited"
        fake_showError.return_value == "an error occured"
        with mock.patch.object(LoadData, 'getInputFilePath', FakeLoadData.fake_getInputFilePath):
            with mock.patch.object(LoadData, 'loadJson', FakeLoadData.fake_loadJson):
                assert LoadData().getInputData() == 'json_loaded: fake input path'

    @mock.patch('src.common.load_data.sys.exit')
    @mock.patch.object(Messages, 'showError')
    def test_getInputDataError(self, fake_sys_exit, fake_showError):
        '''
        Test get input data method calls
        '''

        fake_sys_exit.return_value = "system exited"
        fake_showError.return_value == "an error occured"
        with mock.patch.object(LoadData, 'getInputFilePath', return_value=""),\
            mock.patch.object(LoadData, 'loadJson', FakeLoadData.fake_loadJson):
            assert LoadData().getInputData() == 'system exited'
        
        
        
        # assert LoadData().getInputData() == "system exited"

