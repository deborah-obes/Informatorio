# calculadora_superficies.py
"""
Calculadora de superficies - Tkinter
Soporta: Rectángulo, Círculo, Triángulo, Trapecio, Elipse
Coloca una imagen llamada 'background.png' en la misma carpeta (opcional).
Requiere: Pillow (pip install pillow)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from math import pi
import os

# Intentamos usar PIL para manejar la imagen de fondo
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

# -------------------------
# Funciones de área
# -------------------------
def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return pi * radio * radio

def area_triangulo(base, altura):
    return 0.5 * base * altura

def area_trapecio(base_mayor, base_menor, altura):
    return 0.5 * (base_mayor + base_menor) * altura

def area_elipse(a, b):
    return pi * a * b

# -------------------------
# Interfaz
# -------------------------
class CalculadoraSuperficies(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Superficies")
        self.resizable(False, False)

        # tamaño de ventana
        self.WIDTH = 600
        self.HEIGHT = 420
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # contenedor del canvas de fondo
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Cargar imagen de fondo si está disponible
        self.bg_image = None
        self.bg_photo = None
        self.load_background_image("background.png")

        # Frame semi-transparente para controles (simulación)
        self.frame = tk.Frame(self.canvas, bg="#ffffff", bd=0)
        # Usaremos create_window para ubicar el frame encima del canvas
        self.frame_id = self.canvas.create_window(self.WIDTH//2, self.HEIGHT//2,
                                                  window=self.frame, width=520, height=360)

        self.create_widgets()

    def load_background_image(self, filename):
        if PIL_AVAILABLE and os.path.exists(filename):
            try:
                img = Image.open(filename)
                # redimensionar manteniendo ratio
                img = img.resize((self.WIDTH, self.HEIGHT), Image.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(img)
                self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
            except Exception as e:
                print("Error al cargar la imagen de fondo:", e)
                self.canvas.configure(bg="#f0f0f0")
        else:
            # fallback: fondo liso con degradado lento (simulado con color)
            self.canvas.configure(bg="#e9f7ff")

    def create_widgets(self):
        # Título dentro del frame
        title = tk.Label(self.frame, text="Calculadora de Superficies", font=("Segoe UI", 16, "bold"),
                         bg="#ffffff")
        title.pack(pady=(10, 6))

        subtitle = tk.Label(self.frame, text="Elige una figura y completa las medidas (unidades en metros)",
                            font=("Segoe UI", 9), bg="#ffffff")
        subtitle.pack(pady=(0,8))

        # Selección de figura
        shapes_frame = tk.Frame(self.frame, bg="#ffffff")
        shapes_frame.pack(pady=(4,8))

        self.shape_var = tk.StringVar(value="rectangulo")
        shapes = [("Rectángulo", "rectangulo"),
                  ("Círculo", "circulo"),
                  ("Triángulo", "triangulo"),
                  ("Trapecio", "trapecio"),
                  ("Elipse", "elipse")]

        for text, val in shapes:
            rb = ttk.Radiobutton(shapes_frame, text=text, value=val, variable=self.shape_var, command=self.on_shape_change)
            rb.pack(side="left", padx=6)

        # Área de entradas dinámicas
        self.inputs_container = tk.Frame(self.frame, bg="#ffffff")
        self.inputs_container.pack(pady=(6,10))

        # Crear campos posibles (se mostrarán/ocultarán)
        self.entries = {}
        fields = ["base", "altura", "radio", "base_mayor", "base_menor", "a", "b"]
        labels_map = {
            "base": "Base (m)",
            "altura": "Altura (m)",
            "radio": "Radio (m)",
            "base_mayor": "Base mayor (m)",
            "base_menor": "Base menor (m)",
            "a": "Semieje a (m)",
            "b": "Semieje b (m)"
        }
        for f in fields:
            row = tk.Frame(self.inputs_container, bg="#ffffff")
            lbl = tk.Label(row, text=labels_map[f], width=15, anchor="w", bg="#ffffff")
            ent = ttk.Entry(row, width=18)
            row.pack(fill="x", pady=3)
            lbl.pack(side="left")
            ent.pack(side="left", padx=6)
            self.entries[f] = ent

        # Resultado
        result_frame = tk.Frame(self.frame, bg="#ffffff")
        result_frame.pack(pady=(6,8))
        calc_btn = ttk.Button(result_frame, text="Calcular", command=self.calculate)
        calc_btn.pack(side="left", padx=6)
        clear_btn = ttk.Button(result_frame, text="Limpiar", command=self.clear_all)
        clear_btn.pack(side="left", padx=6)

        self.result_label = tk.Label(self.frame, text="", font=("Segoe UI", 12, "bold"), bg="#ffffff")
        self.result_label.pack(pady=(8,6))

        # Mensaje de ayuda
        ayuda = tk.Label(self.frame,
                         text="Notas: usa números positivos. Separador decimal: punto (.)",
                         font=("Segoe UI", 8), bg="#ffffff")
        ayuda.pack(side="bottom", pady=(4,6))

        # Inicializamos mostrando campos para el rectángulo
        self.on_shape_change()

    def on_shape_change(self):
        shape = self.shape_var.get()
        # Ocultar todos
        for f, ent in self.entries.items():
            ent.master.pack_forget()
        # Mostrar sólo los necesarios
        if shape == "rectangulo":
            self.entries["base"].master.pack(fill="x", pady=3)
            self.entries["altura"].master.pack(fill="x", pady=3)
        elif shape == "circulo":
            self.entries["radio"].master.pack(fill="x", pady=3)
        elif shape == "triangulo":
            self.entries["base"].master.pack(fill="x", pady=3)
            self.entries["altura"].master.pack(fill="x", pady=3)
        elif shape == "trapecio":
            self.entries["base_mayor"].master.pack(fill="x", pady=3)
            self.entries["base_menor"].master.pack(fill="x", pady=3)
            self.entries["altura"].master.pack(fill="x", pady=3)
        elif shape == "elipse":
            self.entries["a"].master.pack(fill="x", pady=3)
            self.entries["b"].master.pack(fill="x", pady=3)
        # Limpiar resultado
        self.result_label.config(text="")

    def parse_positive(self, ent):
        txt = ent.get().strip()
        if txt == "":
            raise ValueError("Campo vacío")
        try:
            val = float(txt)
        except Exception:
            raise ValueError(f"Valor inválido: {txt}")
        if val <= 0:
            raise ValueError("El valor debe ser positivo")
        return val

    def calculate(self):
        shape = self.shape_var.get()
        try:
            if shape == "rectangulo":
                base = self.parse_positive(self.entries["base"])
                altura = self.parse_positive(self.entries["altura"])
                area = area_rectangulo(base, altura)
            elif shape == "circulo":
                radio = self.parse_positive(self.entries["radio"])
                area = area_circulo(radio)
            elif shape == "triangulo":
                base = self.parse_positive(self.entries["base"])
                altura = self.parse_positive(self.entries["altura"])
                area = area_triangulo(base, altura)
            elif shape == "trapecio":
                bm = self.parse_positive(self.entries["base_mayor"])
                bn = self.parse_positive(self.entries["base_menor"])
                altura = self.parse_positive(self.entries["altura"])
                area = area_trapecio(bm, bn, altura)
            elif shape == "elipse":
                a = self.parse_positive(self.entries["a"])
                b = self.parse_positive(self.entries["b"])
                area = area_elipse(a, b)
            else:
                raise ValueError("Figura desconocida")

            # Mostrar con 4 decimales max
            self.result_label.config(text=f"Superficie: {area:.4f} m²")
        except ValueError as ve:
            messagebox.showerror("Error en los datos", str(ve))
        except Exception as e:
            messagebox.showerror("Error", "Ocurrió un error inesperado.\n" + str(e))

    def clear_all(self):
        for ent in self.entries.values():
            ent.delete(0, tk.END)
        self.result_label.config(text="")

# -------------------------
# Ejecutar
# -------------------------
if __name__ == "__main__":
    app = CalculadoraSuperficies()
    app.mainloop()

    
