while True:
    todo_list = []
        user_choice = input( "Enter what you want to do with your todo list (show, add or exit) : ")
        if user_choice.startswith('show'):
            with open('todo.txt', 'r') as file:
                file.readlines()
            for index, item in enumerate(todo_list):
                item = item.strip("\n")
                index = index + 1
                row = f"{index}->{item}"
                print(row)

        elif user_choice.startswith('add'):
            todo_items = user_choice[4:]

            with open('todo.txt', 'r') as file:
                file.readlines()

                todo_list.append(todo_items)

            with open('todo.txt', 'w') as file:
                file.writelines(todo_list)

        elif user_choice.startswith('edit'):
            try:
                number = int(
                    input("Enter the todo's number which you want to edit : "))
                number = number - 1
                edited_todo = input("Please edit this todo")
                todo_list[number] = edited_todo

            except ValueError:
                print('please enter a valid number')
                continue
        elif user_choice.startswith('commplete'):
            try:
                number = int(
                    input("Enter the todo's number which you have completed : "))
                number = number - 1
                todo_list.pop(number)

            except ValueError or IndexError:
                print('please enter a valid number which has a todo task')
                continue
        elif user_choice.startswith('exit'):
            break
