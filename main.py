from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    kilometers_result_label.config(text=f"{round(miles * 1.609)}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=2, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
