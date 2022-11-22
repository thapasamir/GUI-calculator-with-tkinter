from tkinter import *
root = Tk()
#bug fix
#making gemotry
root.wm_iconbitmap('logo.ico')
root.wm_title('SAM_CALC')
root.geometry('290x410') 
root.resizable(0,0)
root.config(bg='black')
#creating entry widgit
enter = Entry(root, border=10,borderwidth=10,width=40)
enter.grid(row=0,column=0,columnspan=3)
#defining clear function
def cls():
	enter.get()
	enter.delete(0, END)
#defining the function which pass the value of button if clicked
def val_pass(num):
	x = enter.get()
	enter.delete(0, END)
	enter.insert(0,str(x)+str(num))
#making add function
def add():
	fisrt_get = enter.get()
	enter.delete(0, END)
	global second_get
	global action
	action = "add"
	second_get = int(fisrt_get)
#makin sub function
def sub():
	fisrt_get = enter.get()
	enter.delete(0, END)
	global second_get
	global action
	action = "sub"
	second_get = int(fisrt_get)
#making mult function
def mult():
	fisrt_get = enter.get()
	enter.delete(0, END)
	global second_get
	global action
	action = "mult"
	second_get = int(fisrt_get)
#making div funcgtion
def div():
	fisrt_get = enter.get()
	enter.delete(0, END)
	global second_get
	global action
	action = "div"
	second_get = int(fisrt_get)
#making equall function
def equall():
	if action == "add":
		final_num = enter.get()
		enter.delete(0, END)
		reasult =int(final_num)+second_get
		enter.insert(0, reasult)
	if action == "sub":
		final_num = enter.get()
		enter.delete(0, END)
		reasult =second_get - int(final_num)
		enter.insert(0, reasult)
	if action == "mult":
		final_num = enter.get()
		enter.delete(0, END)
		reasult =second_get * int(final_num)
		enter.insert(0, reasult)
	if action == "div":
		final_num = enter.get()
		enter.delete(0, END)
		reasult =second_get / int(final_num)
		enter.insert(0, reasult)

#creating button
button1 = Button(root,text="1",padx=40,pady=20,command=lambda: val_pass(1)).grid(row=1,column=0,columnspan=1)
button2 = Button(root,text="2",padx=40,pady=20,command=lambda: val_pass(2)).grid(row=1,column=1,columnspan=1)
button3 = Button(root,text="3",padx=40,pady=20,command=lambda: val_pass(3)).grid(row=1,column=2,columnspan=1)
button4 = Button(root,text="4",padx=40,pady=20,command=lambda: val_pass(4)).grid(row=2,column=0,columnspan=1)
button5 = Button(root,text="5",padx=40,pady=20,command=lambda: val_pass(5)).grid(row=2,column=1,columnspan=1)
button6 = Button(root,text="6",padx=40,pady=20,command=lambda: val_pass(6)).grid(row=2,column=2,columnspan=1)
button7 = Button(root,text="7",padx=40,pady=20,command=lambda: val_pass(7)).grid(row=3,column=0,columnspan=1)
button8 = Button(root,text="8",padx=40,pady=20,command=lambda: val_pass(8)).grid(row=3,column=1,columnspan=1)
button9 = Button(root,text="9",padx=40,pady=20,command=lambda: val_pass(9)).grid(row=3,column=2,columnspan=1)
button0 = Button(root,text="0",padx=40,pady=20,command=lambda: val_pass(0)).grid(row=4,column=0,columnspan=1)
buttonadd= Button(root,text="+",padx=40,pady=20,command=add).grid(row=4,column=1,columnspan=1)
buttonsub= Button(root,text="-",padx=40,pady=20,command=sub).grid(row=4,column=2,columnspan=1)
buttonmult= Button(root,text="X",padx=40,pady=20,command=mult).grid(row=5,column=0,columnspan=1)
buttonndiv = Button(root,text="%",padx=40,pady=20,command=div).grid(row=5,column=1,columnspan=1)
buttonequall = Button(root,text="=",padx=40,pady=20,command=equall).grid(row=5,column=2,columnspan=1)
buttonclear = Button(root,text="clear",padx=80,pady=20,command=cls).grid(row=6,column=0,columnspan=3)
root.mainloop()
