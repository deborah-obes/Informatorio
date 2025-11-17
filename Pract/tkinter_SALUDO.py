import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("App de saludo")
ventana.geometry("300x200")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Escribí tu nombre:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Crear campo de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Función para saludar
def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"¡Hola {nombre}! 👋")

# Botón que ejecuta la función
boton = tk.Button(ventana, text="Saludar", command=saludar, font=("Arial", 12))
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
