class ToDo:
    """
    A class for a single to-do to show whether it has completed
    """
    def __init__(self, name, complete=False):
        self._name = name
        self._complete = complete

    def getName(self):
        return self._name

    def getCompleteInfo(self):
        return self._complete

    def setCompleted(self):
        self._complete = True
