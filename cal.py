from tkinter import *

win = Tk() 
win.geometry("512x424") 
win.resizable(0, 0)
win.title("ماشین حساب")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

 
def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""

 
input_text = StringVar()

 
input_frame = Frame(win, width=512, height=50, bd=0, highlightbackground="red", highlightcolor="blue", highlightthickness=2)
 
input_frame.pack(side=TOP)
 

 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#fff", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) 
 

 
btns_frame = Frame(win, width=512, height=272.5, bg="grey")
 
btns_frame.pack()
 
# ردیف اول
 
clear = Button(btns_frame, text = "C", fg = "Yellow", width = 47, height = 4, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "blue", width = 15, height = 4, bd = 0, bg = "#aaa", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# دریف دوم
 
seven = Button(btns_frame, text = "7", fg = "Green", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "Brown", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "Teal", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "blue", width = 15, height = 4, bd = 0, bg = "#aaa", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# ردیف سوم
 
four = Button(btns_frame, text = "4", fg = "Purple", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "Navy blue", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "Orange", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 15, height = 4, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# ردیف چهارم
 
one = Button(btns_frame, text = "1", fg = "black", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "Fuchsia", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "green", width = 15, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 15, height = 4, bd = 0, bg = "blue", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# ردیف چهارم
 
zero = Button(btns_frame, text = "0", fg = "green", width = 31, height = 4, bd = 0, bg = "Cyan", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

equals = Button(btns_frame, text = "=", fg = "black", width = 15, height = 4, bd = 0, bg = "green", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

point = Button(btns_frame, text = ".", fg = "blue", width = 15, height = 4, bd = 0, bg = "#aaa", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
win.mainloop()
