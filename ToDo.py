class ToDo:
    """
    A class for a single to-do to show whether it has completed
    """
    def __init__(self, name, complete=False):
        self.name = name
        self.complete = complete

    def getName(self):
        return self.name

    def getCompleteInfo(self):
        return self.complete

    def setCompleted(self):
        self.complete = True
