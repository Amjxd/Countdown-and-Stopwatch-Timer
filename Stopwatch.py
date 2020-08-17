# Stop Watch / Count Down
from tkinter import *
import time

# Main Window
root = Tk()
root.title("StopWatch / CountDown")
root.geometry("500x150+900+0")
root.configure(bg='#e6e9ed')
root.resizable(width=False,height = False)

def show_banner(window,text_d):
    upper_banner = Label(window, text = text_d, bg='navy blue',fg = 'white',font=('Helvetica',24),highlightbackground = 'navy blue',width=39,height= 2)
    upper_banner.grid(column=0,row=0,columnspan=2,pady=6)
    lower_banner = Label(window, text = "", bg='navy blue',fg = 'white',font=('arial',20),highlightbackground = 'navy blue',width=46,height= 1)
    lower_banner.grid(column=0,row=4,columnspan=2,pady=6)
show_banner(root,'Stopwatch / Countdown')


# Stop Watch
def update():
    counter.delete(0,END)
    
def display_menu():
    pos_x = root.winfo_x() - 450
    pos_y = root.winfo_y() + 100
    # Creates a new window!
    top = Toplevel()
    top.title('Stop Watch')
    top.configure(bg='#e6e9ed')
    show_banner(top,'StopWatch - Timer' )
    top.resizable(width=False,height = False)
    global counter
    counter = Entry(top,width=20,borderwidth=3,fg='black',font=('arial',35))
    counter.grid(column=0,row=2,columnspan=2,pady=7)
    counter.insert(0,"00:00:00")
    top.geometry(f"500x220+{pos_x}+{pos_y}")
    start = Button(top,text= "START", font = ('arial',14,'bold'),width = 8, command = count_up,highlightbackground = '#e6e9ed')
    stop = Button(top,text= "STOP", font = ('arial',14,'bold'),width = 8, command = count_stop,highlightbackground = '#e6e9ed')
    start.grid(column = 0 ,row = 3,sticky=E)
    stop.grid(column=1,row=3,sticky=W)

s,m,h,q,stop_y_or_n = 0,0,0,0,0
def count_up():
    global q,s,m,h,counter,time,stop_y_or_n
    stop_y_or_n = 1
    if q == 0:
        counter.delete(0,END)
        if s < 10:
            s = "0" + str(s)
        if m < 10:
            m = "0" + str(m)
        if h < 10:
            h = "0" + str(h)
        time = str(h) + ":" + str(m) + ":" + str(s)
        counter.insert(0, time)
        counter.after(1000, count_up) # After Method is like time.sleep but for Tkinter
        s = int(s) + 1
        m = int(m)
        h = int(h)
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
def count_stop():
    global q,time,stop_y_or_n
    if stop_y_or_n == 1:
        q = 1
        counter.delete(0,END)
        counter.insert(0,time)


stopwatch = Button(root,text= "STOPWATCH", font = ('arial',14,'bold'),width = 23, command = display_menu,highlightbackground = '#e6e9ed')
stopwatch.grid(column = 0 , row = 1)

# CountDown

def display_countdown_menu():
    top_b = Toplevel()
    top_b.configure(bg='#e6e9ed')
    top_b.title("CountDown")
    pos_x = root.winfo_x() + 450
    pos_y = root.winfo_y() + 100
    top_b.resizable(width=False,height = False)
    top_b.geometry(f"500x220+{pos_x}+{pos_y}")
    show_banner(top_b,'CountDown - Timer')
    global counter2,start1
    counter2 = Entry(top_b,width=20,borderwidth=3,fg='black',font=('arial',35))
    counter2.grid(column=0,row=2,columnspan=2,pady=7)
    counter2.insert(0,'00:00:00')
    start1 = Button(top_b,text= "BEGIN COUNTDOWN", font = ('arial',17,'bold'),width = 20, command = begin_countdown,highlightbackground = '#e6e9ed')
    start1.grid(column = 0 ,row = 3,sticky=E)
global start
start = 1
def begin_countdown():
    # Grab the displayed amount
    global start
    counter2.config(bg = "white")
    start = 1
    timed = counter2.get()
    zlist = timed.split(":")
    new_lst = []
    for i in zlist:
        i = int(i)
        new_lst.append(i)
    print(new_lst)
    global hr, mn, sc
    hr = new_lst[0]
    mn = new_lst[1]
    sc = new_lst[2]

    # Begin Counting Down
    def counting_start():
        global hr,mn,sc,start
        if start == 1:
            counter2.delete(0,END)
            if sc < 10:
                sc = "0" + str(sc)
            if mn < 10:
                mn = "0" + str(mn)
            if hr < 10:
                hr = "0" + str(hr)
            time = str(hr) + ":" + str(mn) + ":" + str(sc)
            counter2.insert(0, time)
            counter2.after(1000, counting_start) # After Method is like time.sleep but for Tkinter
            sc = int(sc)
            mn = int(mn)
            hr = int(hr)
            if sc == 0 and mn == 0 and hr == 0:
                counter2.config(bg = "red")
                start = 0
            else:
                if sc == 0:
                    sc = 59
                    if mn != 0:
                        mn -= 1
                else:
                    sc -= 1
                if mn == 0:
                    if hr != 0:
                        hr -= 1
                        mn = 60
    counting_start()
        
countdown = Button(root,text= "COUNTDOWN", font = ('arial',14,'bold'),width = 23,highlightbackground = '#e6e9ed', command = display_countdown_menu)
countdown.grid(column=1,row=1)

root.mainloop()
