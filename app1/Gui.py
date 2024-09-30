import functon
import PySimpleGUI as sg

label = sg.Text("Type in a To DO")
input_box = sg.InputText(tooltip="Enter todo", key= "todo")

add_btn = sg.Button("Add")

windows = sg.Window("My To Do App", layout=[[label],
                                            [input_box, add_btn]],
                                            font=("Helvetica", 20))


while True:
    event, value = windows.read()
    print(event, value)

    match event:
        case "Add":
            todos = functon.get_todos()
            new_todos = value['todo']+ "\n"
            todos.append(new_todos)
            functon.write_todos(todos_arg=todos, filepath="todos.txt")

        case sg.WIN_CLOSED:
            break
windows.close()            