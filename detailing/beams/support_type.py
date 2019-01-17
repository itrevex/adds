class SupportType:
    '''
    Defines support type
    support has a column on top and column at the bottom
    Check the column class to see how columns for each
    support type are defined
    '''

    def __init__(self, column_top = None, column_bottom = None):
        self.column_top = column_top
        self.column_bottom = column_bottom

    def setColumnTop(self, column_top):
        self.column_top = column_top

    def setColumnBottom(self, column_bottom):
        self.column_bottom = column_bottom