import tkinter as tk
from tkinter import ttk, messagebox

class VisualizadorMateriales:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Materiales y Costos - Déborah Obes")
        self.root.geometry("700x500")
        self.root.configure(bg="#f2f2f2")

        # --- Datos base de materiales ---
        self.materiales = {
            "Cemento (bolsa)": 5800,
            "Ladrillos comunes (unidad)": 250,
            "Pintura látex (lt)": 3800,
            "Arena (m³)": 5200,
            "Hierro (barra 8mm)": 4500,
            "Cerámica (m²)": 7500
        }

        # --- Encabezado ---
        titulo = tk.Label(self.root, text="Visualizador de Materiales y Costos",
                          font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333333")
        titulo.pack(pady=15)

        # --- Frame de ingreso ---
        frame_ingreso = tk.Frame(self.root, bg="#f2f2f2")
        frame_ingreso.pack(pady=10)

        tk.Label(frame_ingreso, text="Material:", bg="#f2f2f2", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.material_var = tk.StringVar()
        self.combo_material = ttk.Combobox(frame_ingreso, textvariable=self.material_var, values=list(self.materiales.keys()), width=30, state="readonly")
        self.combo_material.grid(row=0, column=1, padx=5)

        tk.Label(frame_ingreso, text="Cantidad:", bg="#f2f2f2", font=("Arial", 12)).grid(row=0, column=2, padx=5)
        self.cantidad_var = tk.StringVar()
        tk.Entry(frame_ingreso, textvariable=self.cantidad_var, width=10).grid(row=0, column=3, padx=5)

        ttk.Button(frame_ingreso, text="Agregar", command=self.agregar_material).grid(row=0, column=4, padx=10)

        # --- Tabla ---
        columnas = ("Material", "Cantidad", "Precio Unitario", "Subtotal")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=150)
        self.tabla.pack(pady=10)

        # --- Frame de botones ---
        frame_botones = tk.Frame(self.root, bg="#f2f2f2")
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Calcular Total", command=self.calcular_total).grid(row=0, column=0, padx=10)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_tabla).grid(row=0, column=1, padx=10)

        # --- Total ---
        self.total_label = tk.Label(self.root, text="Total: $0", font=("Arial", 14, "bold"), bg="#f2f2f2", fg="#1a1a1a")
        self.total_label.pack(pady=10)

    def agregar_material(self):
        material = self.material_var.get()
        cantidad = self.cantidad_var.get()

        if not material or not cantidad.isdigit():
            messagebox.showwarning("Error", "Seleccioná un material y una cantidad válida.")
            return

        cantidad = int(cantidad)
        precio_unitario = self.materiales[material]
        subtotal = cantidad * precio_unitario

        self.tabla.insert("", "end", values=(material, cantidad, f"${precio_unitario}", f"${subtotal}"))

        self.material_var.set("")
        self.cantidad_var.set("")

    def calcular_total(self):
        total = 0
        for item in self.tabla.get_children():
            subtotal_str = self.tabla.item(item, "values")[3]
            subtotal = int(subtotal_str.replace("$", ""))
            total += subtotal
        self.total_label.config(text=f"Total: ${total}")

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        self.total_label.config(text="Total: $0")

# --- Ejecutar la app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizadorMateriales(root)
    root.mainloop()