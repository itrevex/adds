import datetime

class Utils:
    
    now = datetime.datetime.now()

    @staticmethod
    def getNow():
        return datetime.datetime.now()

    @staticmethod
    def dateString():
        '''
        Return date string 
        190111
        '''
        now = Utils.getNow()
        return "%s%02d%02d" %(str(now.year)[-2:], now.month, now.day)

    @staticmethod
    def timeString():
        '''
        Return time string 
        0633
        '''

        now = Utils.getNow()
        return "%02d%02d" %(now.hour, now.minute)

    @staticmethod
    def dateTimeString():
        '''
        Return time string 
        190111_0633
        '''

        return Utils.dateString() + "_" + Utils.timeString()
