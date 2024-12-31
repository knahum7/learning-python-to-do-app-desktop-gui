FILEPATH="todo.txt"

def get_todos(filepath=FILEPATH):
    """ read the contents of a text file and
    return them as a list"""
    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos
def write_todos(todos_arg,filepath=FILEPATH):
    """write the parameter list to a text file"""
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

if __name__=="__main__":
    print("Hello")