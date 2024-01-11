#**************Form**********
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title('تایمر شمارش معکوس')
win.geometry('500x200')
win.resizable(0,0)
win.configure(bg = 'pink')

#*************func************
time = 0

def set_():
    global time 
    time += int(lable_boxtime.get())
    return time

def reset_():
    global time
    time = 0
    # time.set("")
    lable_count.config(text= ' ')
    lable_boxtime.delete(0,END)
    btn_settime.config(state= NORMAL)
    btn_start.config(state=NORMAL)
    

def countdown():
    global time
    if time > 0:
        btn_settime.config(state=DISABLED)
        btn_start.config(state=DISABLED)
        lable_count.config(text= time)
        time -= 1
        lable_count.after(1000 , countdown)
        if time == 0 :
            messagebox.showinfo('شمارش معکوس' , 'زمان شما به اتمام رسیده است')
            btn_settime.config(state=NORMAL)
            btn_start.config(state=NORMAL)
    
#****************wedget************

lable_count = Label(win ,  bg = 'pink' ,font= 'bnazanin 40')
lable_count.place(x= 170 , y = 10)

lable_titr = Label(win , text= "زمان را بر حسب ثانیه وارد کنید:" , bg = 'pink')
lable_titr.place(x=275 , y=80)

lable_boxtime = Entry(win , font = 'arial 10')
lable_boxtime.place(x= 125 , y= 80)

btn_settime = Button(win, text= 'تنظیم زمان' , bg = 'yellow' , fg = 'black' , command= set_)
btn_settime.place(x= 120 , y= 140)

btn_start = Button(win , text= 'شروع' , bg = 'yellow' , fg = 'black' , command= countdown)
btn_start.place(x=250 , y=140)

btn_resettime = Button(win , text = 'تنظیم مجدد' , bg = 'yellow' , fg = 'black' , command=reset_)
btn_resettime.place(x= 350 , y=140)


win.mainloop()