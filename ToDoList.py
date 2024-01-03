from ToDo import ToDo


class ToDoList:
    """
        1. create a current list to track the current to-do's
        2. create a deleted_list to store completed to-do's
    """

    def __init__(self, curr_list=None):
        if curr_list is None:
            curr_list = []
        self.curr_list = curr_list
        self.deleted_list = []

    def getCurrList(self) -> [ToDo]:
        return self.curr_list

    def getDeletedList(self) -> [ToDo]:
        return self.deleted_list

    def addToDo(self, thing: ToDo) -> [ToDo]:
        self.curr_list.append(thing)

    def __len__(self):
        return len(self.curr_list)

    def __getitem__(self, item):
        return self.curr_list[item]
