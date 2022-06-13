







from tkinter import *

window = Tk()
window.title("welcome to my awesome app")
window.configure(bg='yellow')
window.geometry("700x600") #fx the window size


f_name =Label(window, text = "First name", font=("Arial Bold",50))
s_name =Label(window, text = "Second name", font=("Arial Bold",50))
f_name.grid(column = 60, row  = 100)
s_name.grid(column = 60 , row  = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("pop up window")
    top.config(bg = 'red')
    msg=Label(top,text  = "welcome to the pop up" font= '18 ').place
btn = Button(window,text = "click me" ,bg= 'blue' , fg='red' command= open_popup().pack())
btn.grid(column =70 , row = 70)

f_name_box = Entry(window,width=10)
f_name_box.grid(column=180 , row= 100)
s_name_box = Entry(window , width=20)
s_name_box.grid(column = 100 , row= 120)

window.mainloop()