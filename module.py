def show_menu():
    print("options:\n"
          "1)add number \n"
          "2)smallest number \n"
          "3)average of numbers \n"
          "4)largest number \n"
          "5)remove number \n"
          "6)exit")
    option = int(input("Enter your option:"))
    print("*" * 50)
    return option


number_list = []


def add_number():
    print("Enter 5 number")
    number = float(input("Please enter your number:"))
    number_list.append(number)
    return number_list


def smallest_number():
    small = min(number_list)
    print("smallest_number:", small)


def average_number():
    average = sum(number_list) / len(number_list)
    return average


def largest_number():
    large = max(number_list)
    print("largest_number:", large)


def remove_number():
    remove_num = float(input("Enter your number you want to delete:"))
    number_list.remove(remove_num)
    return number_list
