import io

class SharedMocks():
    @staticmethod
    def fake_print(self=None, value = ""):
        return value

    @staticmethod
    def fake_open(self, path="fake path"):
        return io.StringIO("\n*input file\n\nFake line 1\nFake line 2")

    @staticmethod
    def fake_raiseAttributeError(self, encoding=None):
        raise AttributeError("Wrong attribute error test")

    @staticmethod
    def fake_input(self, value = "fake input"):
        return value