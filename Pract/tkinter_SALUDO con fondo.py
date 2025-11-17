import tkinter as tk
from PIL import Image, ImageTk  # para manejar imágenes

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("App de saludo con fondo")
ventana.geometry("400x300")

# Cargar la imagen de fondo
imagen_fondo = Image.open("fondo.jpg")  # reemplazá con tu imagen
imagen_fondo = imagen_fondo.resize((400, 300))  # ajusta al tamaño de la ventana
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para mostrar la imagen
fondo_label = tk.Label(ventana, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear marco transparente encima del fondo
frame = tk.Frame(ventana, bg="#ffffff", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta
etiqueta = tk.Label(frame, text="Escribí tu nombre:", font=("Arial", 12), bg="#ffffff")
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(frame, font=("Arial", 12))
entrada.pack(pady=5)

# Función para saludar
def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"¡Hola {nombre}! 👋")

# Botón
boton = tk.Button(frame, text="Saludar", command=saludar, font=("Arial", 12), bg="#4CAF50", fg="white")
boton.pack(pady=10)

# Etiqueta del resultado
etiqueta_resultado = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="#ffffff")
etiqueta_resultado.pack(pady=10)

# Mostrar la ventana
ventana.mainloop()
