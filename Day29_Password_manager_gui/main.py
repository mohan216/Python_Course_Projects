from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Adding data to file
def add_to_file():
    website_name = T1.get()
    email_username = T2.get()
    password = T3.get()
    l1 = len(website_name)
    l2 = len(email_username)
    l3 = len(password)
    if l1<2 or l1>40 or l2<2 or l2>40 or l3<2 or l3>40:
        T1.delete(0, END)
        T2.delete(0, END)
        T3.delete(0, END)
        messagebox.showinfo(title="Invalid length", message="Please enter input of valid length.")
        return

    is_ok = messagebox.showinfo(title="Check info", message="Are you sure you want to save the details entered?")

    if is_ok:
        with open("data.txt", "a") as pass_manager_file:
            pass_manager_file.write(f"{website_name}|{email_username}|{password}\n")



window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


tabControl = ttk.Notebook(window)
tabControl2 = ttk.Notebook(window)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl2)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.grid(row=0,column=0)#ill="both")

tabControl2.add(tab3, text='Tab 3')
tabControl2.grid(row=0,column=2)

canvas = Canvas(tab1, width=200, height=200)
# Load the image
image = PhotoImage(file="logo.png")

# Create an image item on the canvas
image_item = canvas.create_image(100, 100, image=image)

canvas.grid(row=0, column=1)

l1 = Label(text="Website:")
l2 = Label(text="Email/Username")
l3 = Label(text="Password:")
l1.grid(column=0, row=1)
l2.grid(column=0, row=2)
l3.grid(column=0, row=3)



T1 = Entry(width=52)
T1.grid(column=1, row=1, columnspan=2)
T2 = Entry(width=52)
T2.grid(column=1, row=2, columnspan=2)
T3 = Entry(width=33)
T3.grid(column=1, row=3)

bt1 = Button(tab2, text="hi")
bt1.pack(side="right")

bt2 = Button(tab3, text="hi 2")
bt2.pack(side="top")

generate_password = Button(text="Generate password", width=15)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=44, command=add_to_file)
add.grid(column=1, row=4, columnspan=2)




window.mainloop()