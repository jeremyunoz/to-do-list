from ToDo import ToDo


class ToDoList:
    """
        1. create a current list to track the current uncompleted to-do's
        2. create a deleted_list to store completed to-do's
    """

    def __init__(self, curr_list=None):
        if curr_list is None:
            curr_list = []
        self._curr_list = curr_list
        self._deleted_list = []

    def getCurrList(self) -> [ToDo]:
        return self._curr_list

    def getDeletedList(self) -> [ToDo]:
        return self._deleted_list

    def addToDo(self, thing: ToDo) -> [ToDo]:
        self._curr_list.append(thing)

    def processDeletedToDo(self, thing: ToDo) -> [ToDo]:
        if thing.getCompleteInfo() is True:
            self._deleted_list.append(ToDo)
            self._curr_list.remove(thing)

    def __len__(self):
        return len(self._curr_list)

    def __getitem__(self, item):
        return self._curr_list[item]
