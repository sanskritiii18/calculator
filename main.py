import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Configure mainframe columns to allow the Entry to span
for i in range(3):
 mainframe.columnconfigure(i, weight=1)
mainframe.rowconfigure(0, weight=1)


value_entry = Entry(mainframe, width=7)
value_entry.grid(column=1, row=1, columnspan=3, sticky=(W, E))

def button_click(number):
    current = value_entry.get()
    value_entry.delete(0,tkinter.END)
    value_entry.insert(0,current+str(number))

def calculate():
    expression = value_entry.get()
    try:
        # Evaluate the expression (this will handle simple arithmetic)
        result = eval(expression)

        # Clear the entry widget and insert the result
        value_entry.delete(0, tkinter.END)
        value_entry.insert(0, str(result))
    except Exception as e:
        value_entry.delete(0, tkinter.END)
        value_entry.insert(0, "Error")


btn1 = ttk.Button(mainframe, text="1",command=lambda:button_click(1)).grid(column=1, row=2, sticky=W)
btn2= ttk.Button(mainframe, text="2",command=lambda:button_click(2)).grid(column=2, row=2, sticky=W)
btn3= ttk.Button(mainframe, text="3",command=lambda:button_click(3)).grid(column=3, row=2, sticky=E)
btn4 = ttk.Button(mainframe, text="4",command=lambda :button_click(4)).grid(column=1, row=3, sticky=W)
btn5 =ttk.Button(mainframe, text="5",command=lambda:button_click(5)).grid(column=2, row=3, sticky=W)
btn6 =ttk.Button(mainframe, text="6",command=lambda:button_click(6)).grid(column=3, row=3, sticky=E)
btn7=ttk.Button(mainframe, text="7",command=lambda:button_click(7)).grid(column=1, row=4, sticky=W)
btn8=ttk.Button(mainframe, text="8",command=lambda :button_click(8)).grid(column=2, row=4, sticky=W)
btn9=ttk.Button(mainframe, text="9",command=lambda:button_click(9)).grid(column=3, row=4, sticky=E)


add=ttk.Button(mainframe, text="+",command=lambda:button_click("+")).grid(column=1, row=5, sticky=E)
sub=ttk.Button(mainframe, text="-",command=lambda:button_click("-")).grid(column=2, row=5, sticky=E)
multiply=ttk.Button(mainframe, text="*",command=lambda:button_click("*")).grid(column=3, row=5, sticky=E)
divide=ttk.Button(mainframe, text="/",command=lambda:button_click("/")).grid(column=1, row=6, sticky=E)

btneq = ttk.Button(mainframe, text="=",command=calculate).grid(column=2, row=6, sticky=E)





for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

value_entry.focus()


root.mainloop()