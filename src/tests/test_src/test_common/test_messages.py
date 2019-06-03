import unittest.mock as mock
import sys, inspect

from common.messages import Messages
from tests.test_mocks.shared_mocks import SharedMocks
from tests.test_mocks.test_mocks_common.messages_mocks import MessagesMocks

class TestMessages():
    def test_promptUser(self):
        with mock.patch('builtins.print', SharedMocks.fake_print), \
            mock.patch('builtins.input') as fake_input, \
            mock.patch('src.common.messages.sys.exit') as fake_sys_exit:
            fake_input.return_value = "yes"
            messages = Messages("")
            messages.promptUser()
            fake_input.assert_called()

            #when user prompts for a no, exit system
            fake_input.return_value = "no"
            messages.promptUser()
            fake_sys_exit.assert_called()

    def test_showWarning(self):
        with mock.patch('builtins.print') as fake_print, \
            mock.patch.object(Messages, 'promptUser') as fake_prompt:
            
            Messages.showWarning(mock.Mock())
            fake_prompt.assert_called_once()
            assert fake_print.call_count == 3


    def test_w(self):
        with mock.patch('builtins.print') as fake_print:
            Messages.w(mock.Mock())
            assert fake_print.call_count == 4

    def test_i(self):
        with mock.patch('builtins.print') as fake_print:
            Messages.i()
            assert fake_print.call_count == 1

    def test_info(self):
        with mock.patch('builtins.print') as fake_print:
            Messages.info()
            assert fake_print.call_count == 2

    def test_d(self):
        with mock.patch('builtins.print') as fake_print, \
            mock.patch.object(Messages, 'showLineNumber') as fake_showLineNumer:
            Messages.d()
            assert fake_print.call_count == 2
            fake_showLineNumer.assert_called()

    def test_continuePrompt(self):
        with mock.patch('builtins.print') as fake_print, \
            mock.patch('builtins.input') as fake_input: 
            Messages.continuePrompt("yes")
            fake_input.assert_called_once()
            fake_print.assert_called_once()
            fake_input.assert_called_with("yes")

    def test_showLineNumber(self):
        with mock.patch('builtins.print') as fake_print:
            Messages.showLineNumber()
            assert fake_print.call_count == 2
            
            

