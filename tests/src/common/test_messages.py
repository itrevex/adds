import unittest.mock as mock
import sys

from src.common.messages import Messages
from tests.mocks.shared_mocks import SharedMocks

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
