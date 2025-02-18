import sys
from inspect import stack, getframeinfo

class Messages:
    '''
    Possible errors and warnings

    These are given to the user to make decisions
    '''

    CONTINUE = "Do you wish to continue? y/n \n"
    DEEPER_SECTION = "%s specified for %s is deeper than the beam"

    def __init__(self, message):
        pass

    @staticmethod
    def promptUser():
        print()
        response = input(Messages.CONTINUE)
        if (response.lower() == 'yes' or response.lower() == 'y' or response == ""):
            #continue to detail with the errors
            return
        else:
            print()
            print("Program terminated")
            sys.exit()

    @staticmethod
    def showWarning(warning):
        print()
        print("WARNING!- CODE: %s"%warning.code)
        print(warning.msg)
        Messages.promptUser()
        
    @staticmethod
    def w(warning):
        # Messages.showLineNumber()
        print()
        print("WARNING!- CODE: %s"%warning.code)
        print(warning.msg)
        print()

    @staticmethod
    def i(*arg):
        '''
        More general kind of information
        '''
        print(*arg)

    @staticmethod
    def info(*arg):
        '''
        Information that needs to be highlighted
        '''
        print()
        print(*arg)

    @staticmethod
    def d(*arg):
        print()
        Messages.showLineNumber()
        print(*arg)

    @staticmethod
    def continuePrompt(message):
        print()
        input(message)

    @staticmethod
    def showError(error):
        print()
        print("ERROR!- CODE: %s"%error.code)
        print(error.msg)
        print()
        print("Program terminated")
        sys.exit()

    @staticmethod
    def showLineNumber():
        caller = getframeinfo(stack()[2][0])
        print("File name: ", caller.filename)
        print("line: : ", caller.lineno)