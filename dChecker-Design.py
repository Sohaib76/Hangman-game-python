from tkinter import *


def printtext():
        string = entry.get() 
        st='you have '+string
        searchbutton.place_forget()
        lable.place_forget()
        lable2.place_forget()
        entry.place_forget()
        scrollbar = Scrollbar(main_window)
        scrollbar.pack(side=RIGHT, fill=Y)
       # mylist = Listbox(root, yscrollcommand = scrollbar.set )
       # for line in range(100):
        #   mylist.insert(END, w.cget("text") + str(line))



        
        area = Text(main_window, yscrollcommand = scrollbar.set, font = ('Courier New', 11))
        area.pack(expand=True, fill='both')
        

        scrollbar.config(command=area.yview)



        l3=Label(area,text=st,font='times 50')
        for line in range(1000):
           area.insert(END, l3.cget("text") + str(line))
        
        l3.place(x=50,y=250)



main_window=Tk()
main_window.geometry('1100x650+50+100')
main_window.title('D-Checker')

entry=Entry(main_window,bd=2,relief='raised', width=60)
entry.place(x=340,y=250)
lable=Label(main_window,text='This is a medical search engine.',font='times 30')
lable.place(x=320,y=300)
lable2=Label(main_window,text='D-Checker',fg='green',font='times 110')
lable2.place(x=280,y=80)

searchbutton=Button(main_window,text='search',width=12,height=1,bd=3,relief='raised',command=printtext)
searchbutton.place(x=760,y=246)



main_window.mainloop()
