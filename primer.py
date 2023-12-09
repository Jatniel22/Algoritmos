import tkinter as tk
from clase import calculos
menu=tk.Tk()
menu.geometry("200x300")
def action():
    menu.withdraw()
    promedio=calculos()
    promedio.promedio()
prom=tk.Button(menu, text="PROMEDIO", command= action)

prom.pack()


menu.mainloop()