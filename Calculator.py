from tkinter import *
root = Tk()
root.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="Lucida", width=35, borderwidth=4)
screen.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
button_1 = Button(root, text="1",padx=40, pady=10)
button_1.bind("<Button-1>",button_click)

button_2 = Button(root, text="2",padx=40, pady=10)
button_2.bind("<Button-1>",button_click)

button_3 = Button(root, text="3",padx=40, pady=10)
button_3.bind("<Button-1>",button_click)

button_4 = Button(root, text="4",padx=40, pady=10)
button_4.bind("<Button-1>",button_click)

button_5 = Button(root, text="5",padx=40, pady=10)
button_5.bind("<Button-1>",button_click)

button_6 = Button(root, text="6",padx=40, pady=10)
button_6.bind("<Button-1>",button_click)

button_7 = Button(root, text="7",padx=40, pady=10)
button_7.bind("<Button-1>",button_click)

button_8 = Button(root, text="8",padx=40, pady=10)
button_8.bind("<Button-1>",button_click)

button_9 = Button(root, text="9",padx=40, pady=10)
button_9.bind("<Button-1>",button_click)

button_0 = Button(root, text="0",padx=40, pady=10)
button_0.bind("<Button-1>",button_click)

button_addition = Button(root,text="+",padx=39,pady=10)
button_addition.bind("<Button-1>",button_click)

button_subtraction = Button(root,text="-",padx=39,pady=10)
button_subtraction.bind("<Button-1>",button_click)

button_multiply = Button(root,text="*",padx=39,pady=10)
button_multiply.bind("<Button-1>",button_click)

button_divide = Button(root,text="/",padx=39,pady=10)
button_divide.bind("<Button-1>",button_click)

button_clear = Button(root,text="C",padx=39,pady=10)
button_clear.bind("<Button-1>",button_click)

button_equal = Button(root,text="=",padx=39,pady=10)
button_equal.bind("<Button-1>",button_click)

button_back = Button(root, text= ".",padx=39,pady=10)
button_back.bind("<Button-1>",button_click)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_addition.grid(row=4,column=0)
button_subtraction.grid(row=4,column=1)
button_multiply.grid(row=4,column=2)
button_clear.grid(row=5,column=0)
button_equal.grid(row=5,column =1)
button_back.grid(row=5,column=2)

root.mainloop()