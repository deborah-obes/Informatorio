import tkinter as tk
from tkinter import messagebox

class MapaEspaciosVerdes:
    def __init__(self, root):
        self.root = root
        self.root.title("Mapa Interactivo de Espacios Verdes - Déborah Obes")
        self.root.geometry("800x600")
        
        # Canvas para mostrar el mapa
        self.canvas = tk.Canvas(root, width=780, height=500, bg="white")
        self.canvas.pack(pady=20)
        
        # Cargar imagen de fondo (mapa)
        try:
            self.mapa_img = tk.PhotoImage(file="mapa_resistencia.png")
            self.canvas.create_image(0, 0, anchor="nw", image=self.mapa_img)
        except:
            self.canvas.create_text(390, 250, text="Mapa no disponible", font=("Arial", 24))
        
        # Diccionario de zonas (x1, y1, x2, y2)
        self.zonas = {
            "Plaza 25 de Mayo": {"coords": (50,50,150,150), "superficie":"1200 m²", "vegetacion":"Césped y árboles", "foto":"link_foto_plaza"},
            "Parque de la Democracia": {"coords": (200,100,350,250), "superficie":"5000 m²", "vegetacion":"Árboles, arbustos", "foto":"link_foto_parque"},
            "Costanera": {"coords": (400,300,700,450), "superficie":"10000 m²", "vegetacion":"Palmeras y césped", "foto":"link_foto_costanera"}
        }

        # Dibujar rectángulos invisibles para cada zona
        for zona, info in self.zonas.items():
            x1, y1, x2, y2 = info["coords"]
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="", tags=zona)
            self.canvas.tag_bind(rect, "<Button-1>", self.mostrar_info)

    def mostrar_info(self, event):
        # Determinar qué zona fue clickeada
        item = self.canvas.find_closest(event.x, event.y)
        tags = self.canvas.gettags(item)
        if tags:
            zona = tags[0]
            info = self.zonas.get(zona)
            if info:
                ventana_info = tk.Toplevel(self.root)
                ventana_info.title(zona)
                ventana_info.geometry("350x200")
                
                tk.Label(ventana_info, text=f"Nombre: {zona}", font=("Arial", 12, "bold")).pack(pady=5)
                tk.Label(ventana_info, text=f"Superficie: {info['superficie']}", font=("Arial", 12)).pack(pady=5)
                tk.Label(ventana_info, text=f"Vegetación: {info['vegetacion']}", font=("Arial", 12)).pack(pady=5)
                tk.Label(ventana_info, text=f"Foto/Enlace: {info['foto']}", font=("Arial", 12), fg="blue").pack(pady=5)
            else:
                messagebox.showinfo("Info", "Zona sin información.")
        else:
            messagebox.showinfo("Info", "Zona fuera del área interactiva.")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = MapaEspaciosVerdes(root)
    root.mainloop()
