'''
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''
def get_ext_file(filename):
    return filename.split('.')[1]

filename = input("Enter your filename: ")
print('Extension of file: ', get_ext_file(filename))