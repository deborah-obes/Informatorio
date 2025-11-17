import tkinter as tk
from tkinter import ttk

class GaleriaObras:
    def __init__(self, root):
        self.root = root
        self.root.title("Galería de Obras Arquitectónicas - Déborah Obes")
        self.root.geometry("800x600")
        self.root.configure(bg="#f2f2f2")

        # Lista de obras (pueden agregarse más imágenes y descripciones)
        self.obras = [
            {"titulo": "Casa Minimalista", "anio": 2023, "descripcion": "Residencia unifamiliar con diseño moderno y funcional.", "imagen": "casa_minimalista.png"},
            {"titulo": "Edificio Comercial", "anio": 2022, "descripcion": "Proyecto de oficinas con eficiencia energética.", "imagen": "edificio_comercial.png"},
            {"titulo": "Centro Cultural", "anio": 2021, "descripcion": "Espacio público integrador con áreas verdes y culturales.", "imagen": "centro_cultural.png"}
        ]
        self.index = 0

        # Frame principal
        self.frame = tk.Frame(root, bg="#f2f2f2")
        self.frame.pack(pady=20)

        # Etiqueta de imagen
        self.img_label = tk.Label(self.frame, bg="#f2f2f2")
        self.img_label.pack(pady=10)

        # Etiquetas de texto
        self.titulo_label = tk.Label(self.frame, text="", font=("Arial", 16, "bold"), bg="#f2f2f2")
        self.titulo_label.pack(pady=5)
        self.anio_label = tk.Label(self.frame, text="", font=("Arial", 12), bg="#f2f2f2")
        self.anio_label.pack(pady=2)
        self.desc_label = tk.Label(self.frame, text="", font=("Arial", 12), wraplength=600, bg="#f2f2f2", justify="center")
        self.desc_label.pack(pady=5)

        # Botones de navegación
        self.btn_frame = tk.Frame(self.frame, bg="#f2f2f2")
        self.btn_frame.pack(pady=10)
        self.prev_btn = ttk.Button(self.btn_frame, text="Anterior", command=self.anterior)
        self.prev_btn.pack(side="left", padx=10)
        self.next_btn = ttk.Button(self.btn_frame, text="Siguiente", command=self.siguiente)
        self.next_btn.pack(side="left", padx=10)

        # Cargar la primera obra
        self.mostrar_obra()

    def mostrar_obra(self):
        obra = self.obras[self.index]
        # Cargar imagen (se debe tener en la carpeta los archivos .png)
        try:
            self.img = tk.PhotoImage(file=obra["imagen"])
            self.img_label.config(image=self.img)
        except:
            self.img_label.config(text="Imagen no disponible", image="", font=("Arial", 14))
        
        self.titulo_label.config(text=obra["titulo"])
        self.anio_label.config(text=f"Año: {obra['anio']}")
        self.desc_label.config(text=obra["descripcion"])

    def anterior(self):
        self.index = (self.index - 1) % len(self.obras)
        self.mostrar_obra()

    def siguiente(self):
        self.index = (self.index + 1) % len(self.obras)
        self.mostrar_obra()

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = GaleriaObras(root)
    root.mainloop()
