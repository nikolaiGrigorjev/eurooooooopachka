from tkinter import*
root=Tk()
root.configure(bg="#c2abff")

def newwind(a):
	a1=a.replace(" \n", "")
	#showinfo("tunni informatsioon",f"{a}")
	newwd=Toplevel() #tk()
	abc=Label(newwd,text=Lessons.get(a1),font="Calibri 23",fg="black",justify=CENTER)
	newwd.geometry("500x90")
	abc.pack()


def info(a):
    a_=a.replace(" \n","")
    infokno=Toplevel()
    okowko=Label(infokno,text=uroki.get(a_),font="Arial 26",fg="black",justify=CENTER)
    infokno.geometry("500x150")
    ak.pack()

root=Tk() 
root.title("Check your geography knowledge :) ")
root.iconbitmap('europka.ico')
root.geometry('650x600')
f1=Frame(root,width=150,height=500)
f1.pack(side=LEFT)

var_brov=StringVar()
brov=Checkbutton(fm,text="Брови",font="Calibri 26", fg="blue",variable=var_brov,onvalue="0",offvalue="1",command=brov)
var_glaz1=StringVar()
glaz1=Checkbutton(fm,text="Правый глаз",font="Calibri 26", fg="blue",variable=var_glaz1,onvalue="0",offvalue="1",command=glaz1)
var_glaz2=StringVar()
glaz2=Checkbutton(fm,text="Левый глаз",font="Calibri 26", fg="blue",variable=var_glaz2,onvalue="0",offvalue="1",command=glaz2)
var_rot=StringVar()
rot=Checkbutton(fm,text="Рот",font="Calibri 26", fg="blue",variable=var_rot,onvalue="0",offvalue="1",command=rot)
var_nos=StringVar()
nos=Checkbutton(fm,text="Нос",font="Calibri 26", fg="blue",variable=var_nos,onvalue="0",offvalue="1",command=nos)
brov.pack(side=RIGHT)
rot.pack(side=RIGHT)
nos.pack(side=RIGHT)
glaz1.pack(side=RIGHT)
glaz2.pack(side=RIGHT)
tk.mainloop()
