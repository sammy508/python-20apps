
import functon
import time
# from functions import get_todos, write_todos

print("Import successful!")



now_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now:", now_time)


now_time =  time.strftime("%b %d , %Y %H : %M :%S " )
 
# print("It is now : ",now_time)
user_prompt = "type add, show, complete or exit: "
while True:
    user_action = input(user_prompt).strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functon.get_todos("todos.txt")
        todos.append(todo)
        functon.write_todos(todos, "todos.txt")


    elif user_action.startswith("show"):
        todos = functon.get_todos("todos.txt")

        if not todos:
            print("No todos to show.")
        else:
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}: {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = functon.get_todos("todos.txt")

            if number < 0 or number >= len(todos):
                print("Invalid todo number.")
            else:
                new_todo = input('Enter new todo: ')
                todos[number] = new_todo 

                functon.write_todos(todos, "todos.txt")

        except ValueError:
            print("Your command isn't valid.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1

            todos = functon.get_todos("todos.txt")

            if number < 0 or number >= len(todos):
                print("Invalid todo number.")
            else:
                todo_to_remove = todos[number].strip('\n')
                todos.pop(number)

                functon.write_todos(todos, "todos.txt")

                message = f"Todo '{todo_to_remove}' was removed from the list."
                print(message)

        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("The index you provided is incorrect. Try again!")

    elif user_action.startswith("exit"):
        break
    else:
        print("Command isn't valid.")

print('Goodbye!')
