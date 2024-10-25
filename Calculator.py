import tkinter as tk
import tkinter.messagebox 
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("Calculator by Jacob")
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax error")

def clear():
    entry.delete(0, tk.END)


button1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: myclick(1))
button1.grid(row=1, column=0, pady=2)

button2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2))
button2.grid(row=1, column=1, pady=2)

button3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3))
button3.grid(row=1, column=2, pady=2)

button4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4))
button4.grid(row=2, column=0, pady=2)

button5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5))
button5.grid(row=2, column=1, pady=2)

button6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6))
button6.grid(row=2, column=2, pady=2)

button7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7))
button7.grid(row=3, column=0, pady=2)

button8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8))
button8.grid(row=3, column=1, pady=2)

button9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: myclick(9))
button9.grid(row=3, column=2, pady=2)

button0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0))
button0.grid(row=4, column=1, pady=2)

#mathematical functions' buttons

button_add = tk.Button(master=frame, text='+', padx=15, pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(master=frame, text='-', padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(master=frame, text='*', padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_divide = tk.Button(master=frame, text='/', padx=15, pady=5, width=3, command=lambda: myclick('/'))
button_divide.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=frame, text='clear', padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=frame, text='=', padx=15, pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()