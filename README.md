Topic : a program to display smallest and largest number by using function and store them.  

Input : the number selected by user from the menu and numbers that are taken from user. 
Process :
 module:/
 We define a function called show_menu() to display menu and its options 
are:
 1)enter number 2) smallest number 3) average of numbers 4) largest number 5)remove number 6)exit/
 We give option as input from user and convert it to int(). Output of the function is option. We make a list for number./ 
We define a function called add_number() and We take the numbers as input and convert it to float. so the function append the numbers to number_list. Output of this function is number_list()./ 
We define a function called smallest_number(). small = min(number_list) and display the small./ We define a function called average_number() and calculate the average :
 average = sum(number_list) / len(number_list). Output of this function is average./
 We define a function called largest_number(). 
large = max(number_list) and display the large./
 We define a function called remove_number() and take the remove_num(the number we want to delet) as input and convert it to float and remove that from number_list. Output of this function is number_list()./
 Main:/ 
The program run in an infinite loop until the user enter the option 6.
 If the user select the option 1: the user enter the number./ 
If the user select the option 2: display the smallest number./ 
If the user select the option 3: the average is calculated./
 If the user select the option 4: display the largest number./
 If the user select the option 5: the user enter the number to remove./
 If the user select the option 6: display bye and break.
 else : display invalid option.
