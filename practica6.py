import tkinter as tk
ventana=tk.Tk()  #Crea la ventana
ventana.title("Mi ventana")#Cambiar titulo
ventana.geometry("400x300")#dfinir el tamaño

boton=tk.Button(ventana, text="Continuar")
boton.pack(pady=20)
ventana.mainloop()#mantener la ventana abierta
