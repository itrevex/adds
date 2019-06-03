from unittest import mock

obj = mock.Mock()
obj2 = mock.Mock()

class MessagesMocks():
    @staticmethod
    def fake_getframeinfo(self):
        return { "filename": 'file.dxf', "lineno": 20 }
    
    @staticmethod
    def fake_stack(self):
        return [0,1,[1,2]]

    @staticmethod
    def fake_print(self, obj, obj2):
        return "printed statement"