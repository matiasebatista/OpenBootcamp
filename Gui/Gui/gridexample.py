import tkinter
from tkinter import ttk

window=tkinter.Tk()

window.columnconfigure(0,weight=1)  # (0,0)  (1,0)  (2,0)
window.columnconfigure(1,weight=3)  # (0,1)  (1,1)  (2,1)  primer numero columna segundo cantidad de filas

label = ttk.Label(window,text="Username")
label.grid(column=0,row=0)

username= ttk.Entry(window)
username.grid(column=1,row = 0)

label2 = ttk.Label(window,text="Password")
label2.grid(column=0,row=1)

password= ttk.Entry(window)
password.grid(column=1,row = 1)

#botton
boton = ttk.Button(window, text = "login")
boton.grid(column = 1,row=3)

window.mainloop()