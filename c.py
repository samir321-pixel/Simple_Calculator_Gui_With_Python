__author__ = 'Samir'

import tkinter as tk
import webbrowser
from tkinter import ttk

exp = " "
def press(num):
    global exp
    exp+=str(num)

    equation.set(exp)
def equalpress():
    try:
        global exp
        print(eval(exp))
        total = str(eval(exp))

        equation.set(total)
        exp = " "
    except:
        equation.set('error')
        exp = " "


def clear ():
    global exp
    exp = " "
    equation.set(" ")



if __name__ == "__main__":


    dk = tk.Tk()
    dk.title('Calculator')

    dk.geometry('300x340')
    dk.maxsize(width=270,height=240)

    dk.configure(bg='blue')

    # imp


equation = tk.StringVar()
dis_entry = ttk.Entry(dk,width = 40, state = 'readonly', background ='red', textvariable = equation)
dis_entry.grid(row = 0 , columnspan = 10, ipadx = 6 , ipady = 8)
dis_entry.focus()


btn7 = ttk.Button(dk, text = '7' , width = 5 ,  command = lambda : press(7) )
btn7.grid(row = 1 , column = 0 ,ipady = 4 , ipadx = 2)

btn8 = ttk.Button(dk, text = '8' , width = 5 ,  command = lambda : press(8) )
btn8.grid(row = 1 , column = 1 ,ipady = 4, ipadx = 2)

btn9 = ttk.Button(dk, text = '9' , width = 5 ,  command = lambda : press(9) )
btn9.grid(row = 1 , column = 2,ipady = 4, ipadx = 2)

btnmines = ttk.Button(dk, text = '-' , width = 8 ,  command = lambda : press('-') )
btnmines.grid(row = 1 , column = 3 , ipady = 3, ipadx = 2)

btnmul = ttk.Button(dk, text = '*' , width = 8 ,  command = lambda : press("*") )
btnmul.grid(row = 1 , column = 4 , ipady = 3, ipadx = 2)

btn4 = ttk.Button(dk, text = '4' , width = 5 ,  command = lambda : press(4) )
btn4.grid(row = 2 , column = 0 ,ipady = 4 , ipadx = 2)

btn5 = ttk.Button(dk, text = '5' , width = 5 ,  command = lambda : press(5) )
btn5.grid(row = 2 , column = 1 ,ipady = 4, ipadx = 2)

btn6 = ttk.Button(dk, text = '6' , width = 5 ,  command = lambda : press(6) )
btn6.grid(row = 2 , column = 2,ipady = 4, ipadx = 3)



btnplus = ttk.Button(dk, text = '+' , width = 5 ,  command = lambda : press("+") )
btnplus.grid(row = 2 , column = 3,ipady = 4, ipadx = 10)



btndiv = ttk.Button(dk, text = '/' , width = 5 ,  command = lambda : press("/")  )
btndiv.grid(row = 2 , column = 4,ipady = 4, ipadx = 10)



btnequal = ttk.Button(dk, text = 'Enter' , width = 5,  command = equalpress )
btnequal.grid(row = 3 , column = 4,ipady = 4, ipadx = 10)



btn0= ttk.Button(dk, text = '0' , width = 5,  command = lambda : press(0)  )
btn0.grid(row = 3 , column = 3,ipady = 4, ipadx = 10)



btn3 = ttk.Button(dk, text = '3' , width = 5,  command = lambda : press(3)  )
btn3.grid(row = 3 , column = 0 ,ipady = 4 , ipadx = 2)


btn2 = ttk.Button(dk, text = '2' , width = 5,  command = lambda : press(2)  )
btn2.grid(row = 3 , column = 1 ,ipady = 4, ipadx = 2)

def callback(url):
    webbrowser.open_new(url)



btn1 = ttk.Button(dk, text = '1' , width = 5 ,  command = lambda : press(1) )
btn1.grid(row = 3 , column = 2,ipady = 4, ipadx = 2)


btnclr = ttk.Button(dk, text = 'Clear' , width = 5 ,  command = clear )
btnclr.grid(row = 4 , columnspan = 6,ipady = 4, ipadx = 108)

link1 = ttk.Button(dk, text="GitHub", cursor="hand2")
link1.bind("<Button-1>", lambda e: callback("https://github.com/samir321-pixel"))
link1.grid(row = 5 , columnspan = 6,ipady = 4, ipadx = 108)

btnexit = ttk.Button(dk, text = 'Exit' , width = 5 ,  command = dk.destroy )
btnexit.grid(row = 6 , columnspan = 6,ipady = 4, ipadx = 108)


dk.mainloop()