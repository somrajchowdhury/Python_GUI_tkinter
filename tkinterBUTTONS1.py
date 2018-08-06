from tkinter import *

window = Tk()
window.title('tkinter Buttons')

def callback():
    print('Click!')

# A button with a callback function
b1 = Button(window, text = "OK", command=callback)
b1.grid(row = 1, column = 1, padx = 10, pady = 10)

# A disabled button
b2 = Button(window, text = "Help!", state = DISABLED)
b2.grid(row = 1, column = 2, pady = 10)

'''
To specify the size of the button

(a) We can use the 'padx' and 'pady' option to add some
    extra space between the contents and the button border.

(b) We can also use the 'height' and 'width' options to
    explicity set the size.
'''

b3 = Button(window, text="Click Me!", padx = 10, pady = 10)
b3.grid(row = 1, column = 3, padx = 10, pady = 10)

'''
- Buttons can display multiple lines of text (but only in one font).

- You can use newlines, or use the 'wraplength' option to make the
  button wrap text by itself.

- When wrapping text, use the 'anchor', 'justify' and possibly 'padx'
  options to make things look exactly as you wish.
'''

b4 = Button(window, text='A Button with lots of text. A Big Button. A Huge Button.', wraplength=80, anchor=W, justify=LEFT, padx=2)
b4.grid(row = 1, column = 4, pady = 10)

'''
To make a ordinary button look like it's held down, you can change the
relief from 'RAISED' to 'SUNKEN'.
'''

b5 = Button(window, text="Hello")
b5.config(relief = SUNKEN)
b5.grid(row = 1, column = 5, padx = 10, pady = 10)

'''
To change the color of a button
'''

b6 = Button(window, text='Black Button', bg='black', fg='white')
b6.grid(row = 2, column = 6, pady = 10)

b7 = Button(window, text='Blue Button', bg='blue', fg='white')
b7.grid(row = 3, column = 6, padx = 10, pady = 10)

b8 = Button(window, text='Red Button', bg='red', fg='black')
b8.grid(row = 4, column = 6, pady = 10)

b9 = Button(window, text='Yellow Button', bg='yellow', fg='black')
b9.grid(row = 5, column = 6, padx = 10, pady = 10)

'''
Another way to change the color of button
'''

b10 = Button(window, text='Green Button')
b10.config(bg='green', fg='white')
b10.grid(row = 6, column = 6, pady = 10)

'''
We can use the 'cursor' option to chnage the cursor style whe the mouse hovers
over the button
'''

b11 = Button(window, text='Cursor', cursor='wait')
b11.grid(row = 1, column = 6, padx = 10, pady = 10)

'''
Button Border Styles
'''

# RAISED Buttons
b12 = Button(window, text='raised0', borderwidth=0, relief=RAISED)
b12.grid(row = 2, column = 1, padx = 10, pady = 5)

b13 = Button(window, text='raised1', borderwidth=1, relief=RAISED)
b13.grid(row = 3, column = 1, pady = 5)

b14 = Button(window, text='raised2', borderwidth=2, relief=RAISED)
b14.grid(row = 4, column = 1, padx = 10, pady = 5)

b15 = Button(window, text='raised3', borderwidth=3, relief=RAISED)
b15.grid(row = 5, column = 1, pady = 5)

b16 = Button(window, text='raised4', borderwidth=4, relief=RAISED)
b16.grid(row = 6, column = 1, padx = 10, pady = 5)

# SUNKEN Buttons
b17 = Button(window, text='sunken0', borderwidth=0, relief=SUNKEN)
b17.grid(row = 2, column = 2, padx = 10, pady = 5)

b18 = Button(window, text='sunken1', borderwidth=1, relief=SUNKEN)
b18.grid(row = 3, column = 2, pady = 5)

b19 = Button(window, text='sunken2', borderwidth=2, relief=SUNKEN)
b19.grid(row = 4, column = 2, padx = 10, pady = 5)

b20 = Button(window, text='sunken3', borderwidth=3, relief=SUNKEN)
b20.grid(row = 5, column = 2, pady = 5)

b21 = Button(window, text='sunken4', borderwidth=4, relief=SUNKEN)
b21.grid(row = 6, column = 2, padx = 10, pady = 5)

# RIDGE Border Buttons
b22 = Button(window, text='ridge1', borderwidth=0, relief=RIDGE)
b22.grid(row = 2, column = 3, padx = 10, pady = 5)

b23 = Button(window, text='ridge1', borderwidth=1, relief=RIDGE)
b23.grid(row = 3, column = 3, pady = 5)

b24 = Button(window, text='ridge1', borderwidth=2, relief=RIDGE)
b24.grid(row = 4, column = 3, padx = 10, pady = 5)

b25 = Button(window, text='ridge1', borderwidth=3, relief=RIDGE)
b25.grid(row = 5, column = 3, pady = 5)

b26 = Button(window, text='ridge1', borderwidth=4, relief=RIDGE)
b26.grid(row = 6, column = 3, padx = 10, pady = 5)

# GROOVE Border Buttons
b27 = Button(window, text='groove1', borderwidth=0, relief=GROOVE)
b27.grid(row = 2, column = 4, padx = 10, pady = 5)

b28 = Button(window, text='groove2', borderwidth=1, relief=GROOVE)
b28.grid(row = 3, column = 4, pady = 5)

b29 = Button(window, text='groove3', borderwidth=2, relief=GROOVE)
b29.grid(row = 4, column = 4, padx = 10, pady = 5)

b30 = Button(window, text='groove4', borderwidth=3, relief=GROOVE)
b30.grid(row = 5, column = 4, pady = 5)

b31 = Button(window, text='groove5', borderwidth=4, relief=GROOVE)
b31.grid(row = 6, column = 4, padx = 10, pady = 5)

# SOLID Border Buttons
b32 = Button(window, text='solid0', borderwidth=0, relief=SOLID)
b32.grid(row = 2, column = 5, padx = 10, pady = 5)

b33 = Button(window, text='solid1', borderwidth=1, relief=SOLID)
b33.grid(row = 3, column = 5, pady = 5)

b34 = Button(window, text='solid2', borderwidth=2, relief=SOLID)
b34.grid(row = 4, column = 5, padx = 10, pady = 5)

b35 = Button(window, text='solid3', borderwidth=3, relief=SOLID)
b35.grid(row = 5, column = 5, pady = 5)

b36 = Button(window, text='solid4', borderwidth=4, relief=SOLID)
b36.grid(row = 6, column = 5, padx = 10, pady = 5)

mainloop()
