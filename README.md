# mini-PyRPN
This is a minimalistic calculator, written in Python. It takes advantage of the built-in
Tkinter library, so the code can be run without installing any additional dependencies.

# FUNCTIONALITY:
The program offers the basic operations, along with a factorial and a possibility to delete
the items from the stack. Further functionality will be added soon.

In order to input the number, you have to choose the numbers from the pad and they will appear
on the small field on the right. In order to push the number, click the "Push!" button.
If you made a mistake while typing the number, click the "->" button. If you wish to delete the
last number from the stack, press the "-> (st.)" button.

If you have a proper number of numbers on the stack which meet certain conditions, you can perform
operations on them with appropriate buttons. Keep in mind that, for example, you can't use the
factorial function on the numbers which contain a floating point or are negative. In case of any
unallowed actions, the MessageBox with an information will appear on the screen.

#TO DO:
- Add the support for physical keys.
- Bring more functions to the calculator such as power, modulo or root.
