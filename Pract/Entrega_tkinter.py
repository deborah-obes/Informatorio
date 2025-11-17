import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje(Hola):
    nombre = entry_nombre.get(Deborah)
    if nombre:
        messagebox.showinfo("Saludo", f"Hola {nombre}, ¡bienvenido/a a mi app!")
    else:
        messagebox.showwarning("Atención", "Por favor, ingresa tu nombre.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Proyecto Tkinter - Ejemplo")
ventana.geometry("300x200")
ventana.configure(bg="#e6f2ff")

# Widgets
tk.Label(ventana, text="Ingresa tu nombre:", bg="#e6f2ff").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)
tk.Button(ventana, text="Saludar", command=mostrar_mensaje).pack(pady=10)

ventana.mainloop()

