'''8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]'''
def display_first_last_color(list):
    print(f'{list[0]} {list[len(list)-1]}')

color_list = ["Red","Green","White" ,"Black"]
display_first_last_color(color_list)