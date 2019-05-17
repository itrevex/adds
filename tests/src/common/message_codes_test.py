from src.common.message_codes import MessageCode

class TestLoadData:
    def init(self):
        self.message_code = MessageCode("initiated properly")

    def test_msg(self):
        self.init()
        assert self.message_code.msg == "initiated properly"

    def test_setMsg(self):
        self.init()
        self.message_code.setMsg("message set")
        assert self.message_code.msg == "message set"

    def test_appendMsg(self):
        self.message_code = MessageCode("there %s go")
        self.message_code.appendMsg("you")
        assert self.message_code.msg == "there you go"