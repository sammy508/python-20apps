import functon
import PySimpleGUI as sg

label = sg.Text("Type in a To DO")
input_box = sg.InputText(tooltip="Enter todo",key= "todo")

add_btn = sg.Button("Add")

List_box = sg.Listbox(values=functon.get_todos(),key="todos",
                      enable_events=True,size=[35 ,10])

edit_btn = sg.Button("Edit")

windows = sg.Window("My To Do App", layout=[[label],
                                            [input_box, add_btn],[List_box,edit_btn]],
                                            font=("Helvetica", 20),
                                            )


while True:
    event, values = windows.read()
    print(event, values)

    match event:
        case "Add":
            todos = functon.get_todos()
            new_todos = values['todo']+ "\n"
            todos.append(new_todos)
            functon.write_todos(todos_arg=todos, filepath="todos.txt")
            windows['todos'].update(values = todos)

        case "Edit":
            todo_to_edit = values['todos'][0]   
            new_todo = values['todo']
            todos = functon.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]= new_todo
            functon.write_todos(todos)
            windows["todos"].update(values=todos)

        case 'todos':
            windows["todo"].update(value=values['todos'][0])    



        case sg.WIN_CLOSED:
            break
windows.close()            