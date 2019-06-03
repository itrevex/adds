# from beams.details.all_beams import AllBeams
from src.common.load_data import LoadData
from src.common.messages import Messages
from src.common.message_codes import MessageCode, MessageCodes
from mocks.common.load_data_mocks import LoadDataMocks
from mocks.shared_mocks import SharedMocks
import sys, pytest
import unittest.mock as mock
from json.decoder import JSONDecodeError

class TestLoadData:

    def test_input(self, LoadDataLayerContent):
        assert LoadData().getLayers() == LoadDataLayerContent

    def test_removeComments(self, LoadDataLines):
        lines_stripped = LoadData().removeComments(LoadDataLines[0])
        assert lines_stripped == LoadDataLines[1]

    @mock.patch.object(LoadData, 'getFile', LoadDataMocks.fake_getFile)
    def test_getFile(self):
        assert LoadData().getFile("fake_path") == 'fake_path'

    @mock.patch.object(LoadData, 'loadJson', LoadDataMocks.fake_loadJson)
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
        fake_io_open.side_effect = LoadDataMocks.fake_loadJsonException
        fake_sys_exit.side_effect = LoadDataMocks.fake_loadJsonException
        assert LoadData().loadJson('fake path') is None
    
    def test_loadJson_attribute_exception(self):
        
        with mock.patch('src.common.load_data.json.load') as fake_json_load, \
            mock.patch('src.common.load_data.re.search', SharedMocks.fake_raiseAttributeError), \
            mock.patch.object(MessageCode, 'setMsg') as fake_setMsg, \
            mock.patch.object(MessageCodes, 'ERROR_INPUT_DATA_FORMAT'), \
            mock.patch('src.common.load_data.sys.exit') as fake_sys_exit, \
            mock.patch('src.common.load_data.io.open') as fake_io_open:
            fake_io_open.return_value = "file opened"
            fake_sys_exit.return_value = "System exit"
            fake_setMsg.side_effect = LoadDataMocks.fake_setMsg
            # type(fake_MessageCode.return_value).msg = mock.PropertyMock(return_value="fake error msg")
            fake_json_load.side_effect = LoadDataMocks.fake_loadJsonException
            assert LoadData().loadJson('fake path') is None
               
    @mock.patch.object(LoadData, 'loadJson', LoadDataMocks.fake_loadJsonException)
    def test_LoadJsonException(self):
        # loadJson.side_effect = Exception()
        with pytest.raises(JSONDecodeError) as error:
            assert LoadData().loadJson('{"me":"me"}')
        assert str(error.value) == 'An error occured: line 1 column 5 (char 4)'
    
    @mock.patch.object(LoadData, 'loadJson', LoadDataMocks.fake_loadJsonException)
    @mock.patch('src.common.messages.sys.exit')
    def test_LoadJsonExceptionLogic(self,fake_sys_exit):
        try:
            LoadData().loadJson('input_file')
        except JSONDecodeError:
            pass

    # @mock.patch.object(sys, 'argv', "../../mocks/philip.trad")
    def test_getInputFilePath(self):
        sys.argv = ["me", "../../mocks/philip.trad"]
        # fake_sys_argv.return_value = "../../mocks/philip.trad"
        assert LoadData().getInputFilePath() == None

    # @mock.patch.object(LoadData, 'getFile')
    @mock.patch.object(sys, 'argv', ["d", "e"])
    def test_getInputFilePathElse(self):
        with mock.patch.object(LoadData, 'getFile', LoadDataMocks.fake_getFile):
            assert LoadData().getInputFilePath() == 'e'

    @mock.patch('src.common.load_data.sys.exit')
    @mock.patch.object(Messages, 'showError')
    def test_getInputData(self, fake_sys_exit, fake_showError):
        '''
        Test get input data method calls
        '''

        fake_sys_exit.return_value = "system exited"
        fake_showError.return_value == "an error occured"
        with mock.patch.object(LoadData, 'getInputFilePath', LoadDataMocks.fake_getInputFilePath):
            with mock.patch.object(LoadData, 'loadJson', LoadDataMocks.fake_loadJson):
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
            mock.patch.object(LoadData, 'loadJson', LoadDataMocks.fake_loadJson):
            assert LoadData().getInputData() == 'system exited'
        
    @mock.patch('src.common.load_data.sys.exit') 
    def test_getOutPutFile(self, fake_sys_exit):
        fake_sys_exit.return_value = "system existed"
        with mock.patch('src.common.load_data.os.path.split') as fake_os_path_split, \
            mock.patch('src.common.load_data.os.path.join') as fake_os_path_join:
            fake_os_path_split.return_value = ("head path", "tail.trad")
            fake_os_path_join.side_effect = LoadDataMocks.fake_setMsg

            assert LoadData().getOutPutFile() == 'fake msg'

    @mock.patch('src.common.load_data.sys.exit') 
    def test_getOutPutFileException(self, fake_sys_exit):
        fake_sys_exit.return_value = "system existed"
        with mock.patch('src.common.load_data.os.path.split') as fake_os_path_split, \
            mock.patch('src.common.load_data.os.path.join') as fake_os_path_join:
            fake_os_path_split.return_value = ("head path", "tail.trad")
            fake_os_path_join.side_effect = SharedMocks.fake_raiseAttributeError
            assert LoadData().getOutPutFile() is None
    

    def test_getHeaderAttribs(self, LoadDataHeaderAttribs):
        assert LoadData().getHeaderAttribs() == LoadDataHeaderAttribs
                
    def test_getTextStyles(self, LoadDataTextStyles):
        assert LoadData().getTextStyles() == LoadDataTextStyles

    def test_printData(self):
        with mock.patch('builtins.print') as mock_print:
            mock_print.side_effect = SharedMocks.fake_print
            LoadData().printData()
            mock_print.assert_called()
            assert mock_print.call_count == 3
            
    def test_readTradFile(self):
        with mock.patch.object(LoadData, 'getInputFilePath') as fake_getPath, \
            mock.patch.object(LoadData, 'getFile', LoadDataMocks.fake_getFile),\
            mock.patch('builtins.open', SharedMocks.fake_open):

            assert LoadData().readTradFile() == ["Fake line 1","Fake line 2"]
            fake_getPath.assert_called()
            

            pass
