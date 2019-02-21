from sympy import *
from math import *
from tkinter import *



root = Tk()
root.title("Integral Calculator")
root.geometry("500x600")
root.configure(background="bisque")



txt_input = StringVar()
text = ""

def check():
    y = txt_1.get()
    upper = txt_2.get()
    lower = txt_3.get()
    x = Symbol("x")
    try:
        a = integrate((y) , (x , lower , upper))
        lbl_result["text"]= a
    except:
        a = integrate(y , x)
        lbl_result["text"]= a

def clear(event=None):
        global text
        text = ""
        txt_input.set(text)



lbl_1 = Label(root, text = "Integral Calculator" , font=("arial",40,"bold")
              , fg="Steel Blue" , bg="bisque")
lbl_1.place(x=20 , y=0)

lbl_2 = Label(root, text = "Calculate the Integral of …" , font=("arial",20)
              , bg="bisque")
lbl_2.place(x=20 , y=80)

txt_1 = Entry(root, font="arial" , justify="center" , bd=4 , textvariable=txt_input)
txt_1.place(x=75 , y=140)

lbl_left = Label(root, text = "∫" , font=("arial",16)
              , bg="bisque")
lbl_left.place(x=60 , y=140)

lbl_right = Label(root, text = "dx" , font=("arial",16)
              , bg="bisque")
lbl_right.place(x=270 , y=140)

lbl_upper = Label(root, text = "Upper Limit" , font=("arial",10)
            , bg="bisque")
lbl_upper.place(x=370 , y=140)

txt_2 = Entry(root, font="arial" , justify="center" , width=4)
txt_2.place(x=390 , y=160)

lbl_lower = Label(root, text = "Lower Limit" , font=("arial",10)
            , bg="bisque")
lbl_lower.place(x=370 , y=180)

txt_3 = Entry(root, font="arial" , justify="center" , width=4)
txt_3.place(x=390 , y=200)



btn_sin = Button(root, padx = 4 , pady = 3 , text = "sin" , command = 1
               , width="6" , bg="RosyBrown1")
btn_sin.place(x=80 , y=180)

btn_cos = Button(root, padx = 4 , pady = 3 , text = "cos" , command = 2
               , width="6" , bg="RosyBrown1")
btn_cos.place(x=140 , y=180)

btn_tan = Button(root, padx = 4 , pady = 3 , text = "tan" , command = 3
               , width="6" , bg="RosyBrown1")
btn_tan.place(x=200 , y=180)

btn_csc = Button(root, padx = 4 , pady = 3 , text = "csc" , command = 4
               , width="6" , bg="RosyBrown1")
btn_csc.place(x=80 , y=210)

btn_sec = Button(root, padx = 4 , pady = 3 , text = "sec" , command = 5
               , width="6" , bg="RosyBrown1")
btn_sec.place(x=140 , y=210)

btn_cot = Button(root, padx = 4 , pady = 3 , text = "tan" , command = 6
               , width="6" , bg="RosyBrown1")
btn_cot.place(x=200 , y=210)

btn_pi = Button(root, padx = 4 , pady = 3 , text = "pi(π)" , command = 7
               , width="6" , bg="RosyBrown1")
btn_pi.place(x=80 , y=240)

btn_ln = Button(root, padx = 4 , pady = 3 , text = "ln" , command = 8
               , width="6" , bg="RosyBrown1")
btn_ln.place(x=140 , y=240)

btn_exp = Button(root, padx = 4 , pady = 3 , text = "exp" , command = 9
               , width="6" , bg="RosyBrown1")
btn_exp.place(x=200 , y=240)

btn_pow = Button(root, padx = 4 , pady = 3 , text = "pow(^)" , command = 10
               , width="6" , bg="RosyBrown1")
btn_pow.place(x=80 , y=270)

btn_sqrt = Button(root, padx = 4 , pady = 3 , text = "sq_rt(√)" , command = 11
               , width="6" , bg="RosyBrown1")
btn_sqrt.place(x=140 , y=270)

btn_abs = Button(root, padx = 4 , pady = 3 , text = "abs(| |)" , command = 12
               , width="6" , bg="RosyBrown1")
btn_abs.place(x=200 , y=270)

btn_inv = Button(root, padx = 4 , pady = 4 , text = "inverse" , command = 13
               , width="6" , bg="RosyBrown1")
btn_inv.place(x=80 , y=300)

btn_clr = Button(root, padx = 6 , pady = 4 , text = "Clear" , command = clear
               , width="14" , bg="RosyBrown1")
btn_clr.place(x=140 , y=300)

btn_check = Button(root, height="2" , width="10" , fg="black"
                   ,text = "Calculate" , command = check , font=("arial",12,"bold")
                   , cursor="center_ptr")
btn_check.place(x=120 , y=350)

lbl_3 = Label(root, text = "Result:" , font=("arial",14) , bg="bisque")
lbl_3.place(x=20 , y =420)

lbl_3 = Label(root, text = ".........................................."
              , font=("arial",14) , bg="bisque")
lbl_3.place(x=20 , y =450)

lbl_result = Label(root, text = "" , font=("arial",16) , bg="bisque")
lbl_result.place(x=20 , y =490)



root.mainloop()
