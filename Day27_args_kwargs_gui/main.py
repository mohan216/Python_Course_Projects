# Miles to Kilometers converter

from tkinter import *

window = Tk()
window.title('Interaction window')
#window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

# l1 = Label(text="Test", fg="green", bg="black", font=(24))
# l1.grid(column=0, row=0)
# l1.config(padx=20, pady=20)
#
#
# def my_func():
#     t1 = input1.get()
#     l1.config(text=t1)
#
#
# b1 = Button(text="Click me", command=my_func)
# b1.grid(column=1, row=1)
#
# b2 = Button(text="New Button", command=my_func)
# b2.grid(column=2, row=0)
#
# input1 = Entry(width=40)
# input1.grid(column=3, row=2)
#t1 = input1.get()


def miles_to_km():
    miles = input1.get()
    km = (float(miles) * 1.609)
    l4.config(text=km)


input1 = Entry()
input1.config(width=10)
input1.grid(column=1, row=0)

l1 = Label(text="Miles")
l1.grid(column=2, row=0)

l2 = Label(text="is equal to")
l2.grid(column=0, row=1)

l3 = Label(text="Km")
l3.grid(column=2, row=1)

l4 = Label(text=" ")
l4.grid(column=1, row=1)

B1 = Button(text="Calculate", command=miles_to_km)
B1.grid(column=1, row=2)







window.mainloop()