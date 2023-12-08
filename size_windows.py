
import tkinter as tk

# Crear la ventana principal
windows = tk.Tk()

# Crear una etiqueta con el mensaje
label = tk.Label(windows, text="¡Hello, Tkinter!, I have changed the size of the window.")

# Empaquetar la etiqueta en la ventana
label.pack()

# Ajustar el tamaño de la ventana a 400x300 píxeles
windows.geometry("400x300")

# Iniciar el bucle principal de la aplicación
windows.mainloop()