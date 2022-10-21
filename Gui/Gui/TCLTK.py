import tkinter

window = tkinter.Tk()
label_saludo = tkinter.Label(window,text = "Hola",bg="yellow")
label_saludo.pack(ipadx=50,ipady=50,fill='both')
label_adios = tkinter.Label(window,text = "Adios",bg="yellow")
label_adios.pack(ipadx=100,ipady=50,fill='both')
#abrir una ventana con una etiqueta
#ipad se usa en pack para colocar el tamaño y fill para que llene ancho u largo o both
#bg es para background color
window.mainloop()
