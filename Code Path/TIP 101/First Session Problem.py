""" 
Understand: 

Input: A list of any item

Output: Each item that was listed in the list 

Return cases: No return Cases 

Edge Cases: Print "No Value or List is Empty"



Plan:
 -Ask user for items
 - loops through items in the list
 -prints each item out on a new line
 -ends loop

 """



def print_list():
    lst = input("Enter items separated by commas: ").split(",")
    for item in lst:
        print(item.strip())

print_list()






