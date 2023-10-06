import tkinter as tk

root = tk.Tk()

root.title("Login Form")
root.geometry("600x400")

name_var = tk.StringVar()
passw_var = tk.StringVar()

def submit():
    name=name_var.get()
    password=passw_var.get()

    print("The name is: ", name)
    print("The password is: ", password)

    name_var.set("")
    passw_var.set("")

name_label = tk.Label(root, text='Username')
name_entry = tk.Entry(root, textvariable=name_var)
passw_label = tk.Label(root, text="Password")
passw_entry = tk.Entry(root, textvariable=passw_var, show='*')

submit_btn = tk.Button(root, text="Submit", command = submit)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)

submit_btn.grid(row=2, column=1)

root.mainloop()