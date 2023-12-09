import tkinter as tk

def on_button_click():
    label.config(text="¡Haz clic en el botón!")

# Crear una instancia de la ventana principal
ventana = tk.Tk()

# Configurar el tamaño y el título de la ventana
ventana.geometry("500x300")
ventana.title("primer programa")


# Crear un botón en la ventana
utton = tk.Button(ventana, text="Haz clic aquí", command=on_button_click)
utton.place(x=5, y=15)
texbox=tk.Entry(ventana)
texbox.pack()
# Crear una etiqueta en la ventana
label = tk.Label(ventana, text="¡Hola, Tkinter!")
label.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()