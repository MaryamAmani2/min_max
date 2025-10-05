from module import *

while True:
    choice = show_menu()
    if choice == 1:
        a = add_number()
        print("*" * 50)
    elif choice == 2:
        b = smallest_number()
        print("*" * 50)
    elif choice == 3:
        c = average_number()
        print("average_of_number:", c)
        print("*" * 50)
    elif choice == 4:
        d = largest_number()
        print("*" * 50)
    elif choice == 5:
        e = remove_number()
        print("*" * 50)
    elif choice == 6:
        print("bye")
        break
    else:
        print("invalid option")
