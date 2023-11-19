from tkinter import *

window = Tk()
window.title("This is a Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def convertion():
    km = num_input.get()
    km = 1.609344 * int(km)
    result_label.config(text=km)


mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)


button = Button(text="convert", command=convertion)
button.grid(column=1, row=2)

num_input = Entry(width=10)
num_input.grid(column=1, row=0)

window.mainloop()
