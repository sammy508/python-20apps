# 

 # Functions blueprint

def get_todos(filepath):
    try:
        with open(filepath, 'r') as file_read:
            todosread = file_read.readlines()
        return todosread
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist




def write_todos(filepath,todos_arg):
       with open(filepath, 'w') as file:
            file.writelines(todos_arg)      # this function doesn't return anything

