from tkinter import *
from tkinter import ttk
import tkinter.messagebox
rt = Tk()
rt.title("RPN Calc 1.0 by Shino")
rt.resizable(0, 0)
mf = ttk.Frame(rt)
argument, stacklist = StringVar(), StringVar()
mf.grid(column = 0, row = 0, sticky = (N, W, E, S))
label0 = Label(mf, textvariable = stacklist)
label0.grid(row = 0, columnspan = 3)
label1 = Label(mf, textvariable = argument, background = "white")
label1.grid(row = 0, column = 3)
stack, command, num = [], '', ''
def construct0():
    global num, argument
    if num == '0':
        tkinter.messagebox.showinfo("An error", "Can't begin with a zero.")
    else:
        num += '0'
        argument.set(num)
def construct1():
    global num, argument
    num += '1'
    argument.set(num)
def construct2():
    global num, argument
    num += '2'
    argument.set(num)
def construct3():
    global num, argument
    num += '3'
    argument.set(num)
def construct4():
    global num, argument
    num += '4'
    argument.set(num)
def construct5():
    global num, argument
    num += '5'
    argument.set(num)
def construct6():
    global num, argument
    num += '6'
    argument.set(num)
def construct7():
    global num, argument
    num += '7'
    argument.set(num)
def construct8():
    global num, argument
    num += '8'
    argument.set(num)
def construct9():
    global num, argument
    num += '9'
    argument.set(num)
def constructd():
    global num, argument
    if '.' in num:
        tkinter.messagebox.showinfo("An error", "A dot is used already.")
    elif num == '':
        num += "0."
        argument.set(num)
    else:
        num += '.'
        argument.set(num)
def constructm():
    global num, argument
    if num == '':
        num += '-'
        argument.set(num)
    else:
        tkinter.messagebox.showinfo("An error", "A minus can be put only on the beginning.")
def goback():
    global num, argument
    if num == '':
        tkinter.messagebox.showinfo("An error", "It's empty already.")
    else:
        num = num[:-1]
        argument.set(num)
def delfromstack():
    global stacklist, stack
    if len(stack) == 0:
        tkinter.messagebox.showinfo("An error", "There is nothing on the stack.")
    else:
        stack = stack[:-1]
        if len(stack) == 0:
            stacklist.set('')
        else:
            stacklist.set(', '.join([str(x) for x in stack]))
def push():
    global num, stacklist, argument
    if float(num) % 1 == 0.0:
        stack.append(int(num))
    else:
        stack.append(float(num))
    stacklist.set(', '.join([str(x) for x in stack]))
    argument.set('')
    num = ''
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
def performa():
    global stack
    if len(stack) < 2:
        tkinter.messagebox.showinfo("An error", "At least 2 elements in the stack are required.")
    else:
        stack[-2] = stack[-2] + stack[-1]
        del stack[-1]
        if stack[-1] % 1 == 0.0:
            stack[-1] = int(stack[-1])
        stacklist.set(', '.join([str(x) for x in stack]))
def performs():
    global stack
    if len(stack) < 2:
        tkinter.messagebox.showinfo("An error", "At least 2 elements in the stack are required.")
    else:
        stack[-2] = stack[-2] - stack[-1]
        del stack[-1]
        if stack[-1] % 1 == 0.0:
            stack[-1] = int(stack[-1])
        stacklist.set(', '.join([str(x) for x in stack]))
def performm():
    global stack
    if len(stack) < 2:
        tkinter.messagebox.showinfo("An error", "At least 2 elements in the stack are required.")
    else:
        stack[-2] = stack[-2] * stack[-1]
        del stack[-1]
        if stack[-1] % 1 == 0.0:
            stack[-1] = int(stack[-1])
        stacklist.set(', '.join([str(x) for x in stack]))
def performd():
    global stack
    if len(stack) < 2:
        tkinter.messagebox.showinfo("An error", "At least 2 elements in the stack are required.")
    else:
        if stack[-1] == 0:
            tkinter.messagebox.showinfo("An error", "The divisior is 0, can't perform the division.")
        else:
            stack[-2] = int((stack[-2] / stack[-1]) * 1000000 + 0.5) / 1000000.0
            del stack[-1]
            if stack[-1] % 1 == 0.0:
                stack[-1] = int(stack[-1])
            stacklist.set(', '.join([str(x) for x in stack]))
def performf():
    global stack
    if len(stack) < 1:
        tkinter.messagebox.showinfo("An error", "At least 1 element in the stack are required.")
    elif type(stack[-1]) != int:
        tkinter.messagebox.showinfo("An error", "The type of an argument is not an integer.")
    elif stack[-1] < 0:
        tkinter.messagebox.showinfo("An error", "Unable to factor a negative number.")
    elif stack[-1] > 25:
        tkinter.messagebox.showinfo("An error", "The number is too large.")
    else:
        stack[-1] = factorial(stack[-1])
        stacklist.set(', '.join([str(x) for x in stack]))
bt0 = Button(mf, text = "7", command = construct7, width = 5, height = 2)
bt1 = Button(mf, text = "8", command = construct8, width = 5, height = 2)
bt2 = Button(mf, text = "9", command = construct9, width = 5, height = 2)
bt3 = Button(mf, text = "+", command = performa, width = 5, height = 2)
bt4 = Button(mf, text = "4", command = construct4, width = 5, height = 2)
bt5 = Button(mf, text = "5", command = construct5, width = 5, height = 2)
bt6 = Button(mf, text = "6", command = construct6, width = 5, height = 2)
bt7 = Button(mf, text = "-", command = performs, width = 5, height = 2)
bt8 = Button(mf, text = "1", command = construct1, width = 5, height = 2)
bt9 = Button(mf, text = "2", command = construct2, width = 5, height = 2)
bt10 = Button(mf, text = "3", command = construct3, width = 5, height = 2)
bt11 = Button(mf, text = "*", command = performm, width = 5, height = 2)
bt12 = Button(mf, text = "0", command = construct0, width = 5, height = 2)
bt13 = Button(mf, text = ".", command = constructd, width = 5, height = 2)
bt14 = Button(mf, text = "!", command = performf, width = 5, height = 2)
bt15 = Button(mf, text = "/", command = performd, width = 5, height = 2)
bt16 = Button(mf, text = "Push!", command = push, width = 5, height = 2)
bt17 = Button(mf, text = "neg", command = constructm, width = 5, height = 2)
bt18 = Button(mf, text = "<-", command = goback, width = 5, height = 2)
bt19 = Button(mf, text = "<- (st)", command = delfromstack, width = 5, height = 2)
bt0.grid(column = 0, row = 2)
bt1.grid(column = 1, row = 2)
bt2.grid(column = 2, row = 2)
bt3.grid(column = 3, row = 2)
bt4.grid(column = 0, row = 3)
bt5.grid(column = 1, row = 3)
bt6.grid(column = 2, row = 3)
bt7.grid(column = 3, row = 3)
bt8.grid(column = 0, row = 4)
bt9.grid(column = 1, row = 4)
bt10.grid(column = 2, row = 4)
bt11.grid(column = 3, row = 4)
bt12.grid(column = 0, row = 5)
bt13.grid(column = 1, row = 5)
bt14.grid(column = 2, row = 5)
bt15.grid(column = 3, row = 5)
bt16.grid(column = 3, row = 1)
bt17.grid(column = 2, row = 1)
bt18.grid(column = 1, row = 1)
bt19.grid(column = 0, row = 1)
rt.mainloop()
