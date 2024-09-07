user_prompt = "type add, show, cmplete or exit: "
todos=[]
while True:
    user_action = input(user_prompt)
    user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter todo: ')+"\n"

        # crete a todo files and store data into todo file

            file = open('todos.txt','r')
            todos= file.readlines()
            file.close()
            todos.append(todo)

            file= open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        #case 'show'| 'display':   bitwise operator
        case 'show':      
            for index, item in  enumerate(todos):
                print(f"{index+1}:{item}")
        
        case 'edit':
            number = int(input('enter tne num you want to edit: '))
            number = number -1
            new_todo = input('enter new todo: ')
            todos[number]=new_todo

        case 'comlete':
            number = int(input('enter tne num you want to remove: '))
            todos.pop(number-1)


        case 'exit':
            break
print('bye bye mf')        


