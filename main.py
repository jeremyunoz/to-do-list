from ToDoList import ToDoList
from ToDo import ToDo

if __name__ == '__main__':
    to_do_list = []
    while 1:
        to_do_list.append(ToDo(input("Please enter your to-do: ")))
        if len(to_do_list) == 2:
            break
    t1 = ToDoList(to_do_list)

    for i in range(0, len(t1)):
        print(t1[i].getName())
