#################from tkinter import *
from tkinter import *
window = Tk()
window.title("welcome to my awesome app")
window.configure(bg='yellow')
window.geometry("700x600") #fx the window size
window.mainloop()

f_name =Label(window, text = "First name " , font=("Arial Bold",50))
s_name =Label(window, text = "Second name " , font=("Arial Bold",50))
f_name.grid(column = 30 , row  = 30)
s_name.grid(column = 30 , row  = 60)
window.mainloop()
btn = Button(window,text = "click me" ,bg= 'blue' , fg='red')
btn.grid(colum =70 , row = 70)

txt_box = Entry(window , width=20)
txt_box.grid(column = 100 , row= 120)##
