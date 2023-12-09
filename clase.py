import tkinter as tk
class calculos:
    def promedio():
        ventana=tk.Tk()
        ventana.geometry("500x200")
        def on_button_click():
            valor=float(campo.get())
            val1=float(campo1.get())
            val2=float(campo2.get())
            sum=float((val1+valor+val2)//3)
            label3.config(text=sum)
                #etiquetas
        label=tk.Label(ventana, text="numero1")
        label1=tk.Label(ventana, text="num2")
        label1.place(x=5, y=40)
        label.place(x=5, y=10)
        label2=tk.Label(ventana, text="num3")
        label2.place(x=5, y=70)
        label3=tk.Label(ventana, text="0000")
        label3.place(x=100, y=20)
        label3.pack()
        #textbox
        campo=tk.Entry(ventana)
        campo.place(x=70, y=10,width=50)
        campo1=tk.Entry(ventana)
        campo1.place(x=70, y=40,width=50)
        campo2=tk.Entry(ventana)
        campo2.place(x=70, y=70,width=50)

        #boton
        entrada=tk.Button(text="calcular", command=on_button_click)
        entrada.place(x=15, y=100)
        ventana.mainloop()





        
