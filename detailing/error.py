class ErrorMessage:
    '''
    Possible errors and warnings

    These are given to the user to make decisions
    '''

    CONTINUE = "Do you wish to continue with error in input?"
    DEEPER_SECTION = "%s specified for %s is deeper than the beam"

    def __init__(self, message):
        self.message

    def promptUser(self, response):
        print(ErrorMessage.CONTINUE)
        if (response == 'YES'):
            #continue to detail with the errors
            pass

    def showWarning(message):
        print(message)
