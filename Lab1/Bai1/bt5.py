#5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
def print_full_name(firstname, lastname):
    print(lastname+' '+firstname)

lname = input('Enter your last name: ')
fname = input('Enter your first name: ')

print_full_name(fname, lname)