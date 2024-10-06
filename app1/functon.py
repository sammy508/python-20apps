# # 

#  # Functions blueprint
Filepath = "todos.txt"

def get_todos(filepath = Filepath):
    try:
        with open(filepath, 'r') as file_read:
            todosread = file_read.readlines()
            
        return todosread
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist




def write_todos(todos_arg,filepath=Filepath):
       with open(filepath, 'w') as file:
            file.writelines(todos_arg)    # this function doesn't return anything


if __name__ == "__main__" :
     print("hello")
     print(get_todos)


