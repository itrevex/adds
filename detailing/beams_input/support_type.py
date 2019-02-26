class SupportType:
    '''
    Defines support type
    support has a column on top and column at the bottom
    Check the column class to see how columns for each
    support type are defined
    '''
    NAME = 1
    def __init__(self, name, column_top = None, column_bottom = None):
        self.name = name
        self.column_top = column_top #column object see column class
        self.column_bottom = column_bottom

    def setColumnTop(self, column_top):
        self.column_top = column_top

    def setColumnBottom(self, column_bottom):
        self.column_bottom = column_bottom

    
    def toString(self):
        string = "\nSupport - " + self.name
        string += "\nColumn Top" + self.column_top.toString()
        string += "\nColumn Bottom" + self.column_bottom.toString()

        return string



        