import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os

# =======================
# Funciones
# =======================
def abrir_album(url):
    webbrowser.open(url)

def abrir_maps(lugar, categoria):
    busqueda = f"{categoria} cerca de {lugar} Corrientes"
    url = f"https://www.google.com/maps/search/{busqueda.replace(' ', '+')}"
    webbrowser.open(url)

# =======================
# Configuración base
# =======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

albumes = [
    {
        "nombre": "Parque 2 de Febrero",
        "imagen": "parque.jpg",
        "enlace": "https://photos.google.com/share/AF1QipMdTJhWieCycslhbDi-TGHhUJpMLh5HBJtrV_SKZcx-1md86xVxDhgiH0fhORj4Ig?key=YW1sMVFMNXYxWlRISTYtQWJQdjhUU0t1YjZkVXpR"
    },
    {
        "nombre": "Plaza de los Abuelos",
        "imagen": "plaza.jpg",
        "enlace": "https://photos.google.com/share/AF1QipMiC48nkng_zHslWXoj5yHTBLOqdXovGZoqOUmUFe3e-gVcBATEs84Jfj33TmpyiQ?key=NzFLdmNfd2xGSEU1TGdiQzg5UXRqVkFaZDh0VzdR"
    },
    {
        "nombre": "Plazoleta San Martín",
        "imagen": "plazoleta.jpg",
        "enlace": "https://photos.google.com/share/AF1QipNatt5t-g5G7tHOwQBSb10A4pHR-Rw6eII8KTFZjULxgBSRDDuDGXPl4CAlKvxOmw?key=Y3NnX1JfMmY4YUw4WGpZS1FKWl9XVzY1bHN4TE1n"
    },
    {
        "nombre": "Sendero Laguna Argüello",
        "imagen": "sendero.jpg",
        "enlace": "https://photos.google.com/share/AF1QipND74qYD1MtP8fAbeYc4wA6V8dyKUVpEwIN1DzhU-pDM2VjLD2EK4Aovw-rUlHC3g?key=R1Zmc1BzV0hXV0RPd3ZOVDNMRHZINTREUHdfbFB3"
    }
]

# =======================
# Interfaz principal
# =======================
ventana = tk.Tk()
ventana.title("Catálogo de Álbumes - Déborah Obes")
ventana.configure(bg="#E8EAFE")
ventana.geometry("950x900")

# ============ Scroll general ============
contenedor_scroll = tk.Canvas(ventana, bg="#E8EAFE", highlightthickness=0)
barras = tk.Scrollbar(ventana, orient="vertical", command=contenedor_scroll.yview)
contenedor_scroll.configure(yscrollcommand=barras.set)

frame_principal = tk.Frame(contenedor_scroll, bg="#E8EAFE")
contenedor_scroll.create_window((0, 0), window=frame_principal, anchor="nw")

contenedor_scroll.pack(side="left", fill="both", expand=True)
barras.pack(side="right", fill="y")

# Actualiza scroll
frame_principal.bind(
    "<Configure>", lambda e: contenedor_scroll.configure(scrollregion=contenedor_scroll.bbox("all"))
)

# ============ Título ============
titulo = tk.Label(
    frame_principal, text="Catálogo Turístico", font=("Helvetica", 26, "bold"),
    bg="#E8EAFE", fg="#1B1B3A"
)
titulo.pack(pady=25)

# ============ Contenedor de álbumes ============
frame_albumes = tk.Frame(frame_principal, bg="#E8EAFE")
frame_albumes.pack(pady=10)

# ============ Tarjetas ============
for i, album in enumerate(albumes):

    ruta_imagen = os.path.join(BASE_DIR, album["imagen"])

    try:
        img = Image.open(ruta_imagen).resize((330, 260))
        foto = ImageTk.PhotoImage(img)
    except:
        foto = tk.PhotoImage(width=330, height=260)
        foto.put("#CCCCCC", to=(0, 0, 330, 260))

    # Tarjeta
    tarjeta = tk.Frame(
        frame_albumes,
        bg="white",
        bd=3,
        relief="groove",
        padx=15,
        pady=15,
        highlightbackground="#AAB0FF",
        highlightthickness=1
    )
    tarjeta.grid(row=i//2, column=i%2, padx=35, pady=25)

    # Imagen con hover
    def on_enter(e, w=tarjeta): w.config(bg="#F7F8FF")
    def on_leave(e, w=tarjeta): w.config(bg="white")

    tarjeta.bind("<Enter>", on_enter)
    tarjeta.bind("<Leave>", on_leave)

    etiqueta_imagen = tk.Label(tarjeta, image=foto, bg="white", cursor="hand2")
    etiqueta_imagen.image = foto
    etiqueta_imagen.pack()
    etiqueta_imagen.bind("<Button-1>", lambda e, url=album["enlace"]: abrir_album(url))

    # Título
    tk.Label(
        tarjeta,
        text=album["nombre"],
        font=("Helvetica", 14, "bold"),
        bg="white",
        fg="#2C2C54"
    ).pack(pady=10)

    # Botones
    botones = tk.Frame(tarjeta, bg="white")
    botones.pack(pady=5)

    for tema in ["Gastronomía", "Bares", "Cultura"]:
        tk.Button(
            botones,
            text=tema,
            font=("Helvetica", 10),
            bg="#DDE3FF",
            fg="#111",
            padx=10,
            pady=3,
            cursor="hand2",
            relief="raised",
            command=lambda t=tema, l=album["nombre"]: abrir_maps(l, t)
        ).pack(side="left", padx=5)

# ============ Pie de página ============
tk.Label(
    frame_principal,
    text="Realizado por: Déborah Obes",
    font=("Helvetica", 11, "italic"),
    bg="#E8EAFE",
    fg="#333"
).pack(pady=20)

ventana.mainloop()
