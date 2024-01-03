from ToDo import ToDo
from ToDoList import ToDoList

class UserInterface:
    def processTodoList(self):
        to_do_list = ToDoList()
        while 1:
            command = input("Choose following commands by enter the number: 1.Add a to-do 2.Complete a to-do 3.Exit: ")
            if command.isdigit():
                command = int(command)
            else:
                continue
            if command == 1:
                toDo = ToDo(input("Please enter the to-do: "))
                to_do_list.addToDo(toDo)
            elif command == 2:
                completed_task = ToDo(input("Please enter the completed to-do: "))
                if len(to_do_list) < 1:
                    print("Invalid approach")
                    continue
                for task in to_do_list:
                    if task.getName() == completed_task.getName():
                        if task.getCompleteInfo() is False:
                            task.setCompleted()
                            to_do_list.processDeletedToDo(task)
                            print("Task completed")
                            break
            elif command == 3:
                print("Thanks for using this to-do-list!")
                break
            else:
                print("Invalid command")
                continue
