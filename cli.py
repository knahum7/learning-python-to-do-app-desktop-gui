import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
user_prompt = ("Type add, show, edit, complete or exit")

while True:
    user_action = input(user_prompt)
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo=user_action[4:]+"\n"
        todos=functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos=functions.get_todos()
        for index,item in enumerate(todos):
            item=item.strip("\n")
            row=f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])-1
            new_todo=input("What is the new todo")+"\n"
            todos=functions.get_todos()
            todos[number]=new_todo
            functions.write_todos(todos)
        except ValueError:
            print("Your command should be the item number")
            continue

    elif user_action.startswith("complete"):
        try:
            completed_task=int(user_action[9:])
            todos=functions.get_todos()
            print(f"Todo {todos[completed_task-1].strip("\n")} was removed from the list")
            todos.pop(completed_task - 1)
            functions.write_todos(todos)
            continue

        except IndexError:
            print("Item number does not exist")

    elif user_action.startswith("exit"):
        break
    else:
        print("undefined command")

print("Bye")
