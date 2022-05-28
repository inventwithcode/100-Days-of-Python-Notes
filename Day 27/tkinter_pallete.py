from tkinter import *

window = Tk()
window.title("inventwithcode")
window.minsize(width=600, height=400)

# Label
my_label = Label(text="Winchester", font=("Arial", 24))
my_label.pack()


def button_clicked():
    my_label["text"] = input.get()
    # input.config(width=10)
    # my_label.config(text="I was clicked!") # We can also use this.


# Button
button = Button(text="Click Me!", command=button_clicked)
button.pack()


# Entry
input = Entry(width=20)
input.pack()


# Entry with filled text
text = Entry(width=30)
text.insert(END, string="Some text to begin with")
print(text.get())
text.pack()


# Text Box
textBox = Text(height=10, width=20)
textBox.insert(END, "Example of multiline text entry. Write inside me!")
textBox.focus()
textBox.pack()
print(textBox.get(1.0, END))


# SpinBox
def spinBox_used():
    print(spin_box.get())


spin_box = Spinbox(from_=0, to=100, width=5, command=spinBox_used)
spin_box.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckButton
def check_button_used():
    print(checked_state.get())


checked_state = IntVar()
check_button = Checkbutton(
    text="Is on?", variable=checked_state, command=check_button_used)
check_button.pack()


# Radio Button
def radio_btn_used():
    print(radio_state.get())


radio_state = IntVar()
radio1 = Radiobutton(text="Dean Winchester", value=1,
                     variable=radio_state, command=radio_btn_used)
radio2 = Radiobutton(text="Sam Winchester", value=2,
                     variable=radio_state, command=radio_btn_used)
radio1.pack()
radio2.pack()


# ListBox

def listBox_used(event):
    print(listBox.get(listBox.curselection()))


listBox = Listbox(height=4)
names = ["Dean", "Sam", "Crowley", "Castiel"]
for hunter in names:
    listBox.insert(names.index(hunter), hunter)
listBox.bind("<<ListboxSelect>>", listBox_used)
listBox.pack()
window.mainloop()
