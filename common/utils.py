import datetime

class Utils:
    
    now = datetime.datetime.now()

    def __init__(self):
        pass

    @staticmethod
    def dateString():
        '''
        Return date string 
        190111
        '''

        return "%s%02d%d" %(str(Utils.now.year)[-2:], Utils.now.month, Utils.now.day)

    @staticmethod
    def timeString():
        '''
        Return time string 
        0633
        '''

        now = datetime.datetime.now()
        return "%02d%02d" %(Utils.now.hour, Utils.now.minute)

    @staticmethod
    def dateTimeString():
        '''
        Return time string 
        190111_0633
        '''

        return Utils.dateString() + "_" + Utils.timeString()

    @staticmethod
    def checkBuild(app_data):
        pass