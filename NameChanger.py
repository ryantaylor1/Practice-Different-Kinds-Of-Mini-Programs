def add_name(names):
    names.append(input("Enter a name to add: "))

def change_name(names):
    name = input("Enter the name to change: ")
    if name in names:
        names[names.index(name)] = input("Enter the new name: ")
    else:
        print("Name not found.")

def delete_name(names):
    try:
        names.remove(input("Enter the name to delete: "))
    except ValueError:
        print("Name not found.")

def view_names(names):
    print("Names :")

def menu():
    names = []
    menu = {"1": add_name, "2": change_name, "3": delete_name, "4": view_names}
    
    while True:
        choice = input("\nMenu:\n1. Add\n2. Change\n3. Delete\n4. View\n5. Exit\nChoose an option: ")
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice](names)
        else:
            print("Invalid choice.")

menu()
