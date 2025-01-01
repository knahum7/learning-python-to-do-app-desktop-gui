import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a To-do")
input_box=sg.InputText(tooltip="Enter Todo",key="todo")
add_button=sg.Button("Add")

window=sg.Window("My To-Do App",
                 layout=[[label],[input_box,add_button]],
                 font=("Helvetica",20))
while True:
    event,value=window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value["todo"]+"\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()

#        case "Show":
#            todos = functions.get_todos()
#            for index, item in enumerate(todos):
#                item = item.strip("\n")
#                row = f"{index + 1}-{item}"
#                print(row)
#        case "Edit":
#            try:
#                todos = functions.get_todos()
#                todos[number] = value
#                functions.write_todos(todos)
#            except ValueError:
#                print("Your command should be the item number")
#        case "Complete":
#            try:
#                todos = functions.get_todos()
#                print(f"Todo {todos[completed_task - 1].strip("\n")} was removed from the list")
#                todos.pop(completed_task - 1)
#                functions.write_todos(todos)
#            except IndexError:
#                print("Item number does not exist")
#        case "Exit":
#                print("Bye")
