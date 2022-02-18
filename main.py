import tkinter

window = tkinter.Tk()
window.title("Miles to Kilo Converter")
window.minsize(150, 100)

#Label

instructions = tkinter.Label(text="Convert Miles to Kilometres", font=("Arial", 10, "bold"))
instructions.grid(column=1,row=0)

my_label = tkinter.Label(text="", font=("Arial", 10, "bold"))
my_label.grid(column=1,row=2)

my_label1 = tkinter.Label(text="Miles", font=("Arial", 10, "bold"))
my_label1.grid(column=2,row=1)

#my_label["text"] = "Doom Gui"
#my_label.config(text="Gui bitches")

#button

def button_clicked():
    my_label["text"] = f"{input.get()} miles is {str(int(input.get()) * 1.609344)} kilometres"

button = tkinter.Button(text= "Convert", command=button_clicked)
button.grid(column=0,row=1)

#entry

input = tkinter.Entry(width=10)
input.grid(column=1,row=1)








window.mainloop()