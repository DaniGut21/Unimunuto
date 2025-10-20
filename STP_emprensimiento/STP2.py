# smarttrack_prototipo.py
# Prototipo SmartTrack Parking - Tkinter (estilo blanco / azul claro)
# Autor: Generado por ChatGPT para Daniel
# Requisitos: pillow (PIL)
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# -------------------------
# Datos simulados (parqueaderos)
# -------------------------
parkings = [
    {
        "id": 1,
        "name": "City Parking Centro",
        "address": "Calle 26 #13-45, Centro",
        "rate_car_per_hour": 6000,     # COP / hora (simulado)
        "rate_moto_per_hour": 3000,
        "rating": 4.2,
        "reviews": [
            {"stars": 4, "text": "Buena ubicación."},
            {"stars": 5, "text": "Servicio rápido."}
        ]
    },
    {
        "id": 2,
        "name": "GeoParking Norte",
        "address": "Av. Suba #120-10, Suba",
        "rate_car_per_hour": 5000,
        "rate_moto_per_hour": 2500,
        "rating": 3.8,
        "reviews": [
            {"stars": 4, "text": "Cómodo pero pequeño."},
            {"stars": 3, "text": "A veces lleno."}
        ]
    },
    {
        "id": 3,
        "name": "Parqueadero Titán Plaza",
        "address": "Cra 15 #80-20, Usme (centro comercial)",
        "rate_car_per_hour": 7000,
        "rate_moto_per_hour": 3500,
        "rating": 4.5,
        "reviews": [
            {"stars": 5, "text": "4 horas gratis con compra."},
            {"stars": 4, "text": "Seguro y limpio."}
        ]
    },
    {
        "id": 4,
        "name": "Parking Mall Occidente",
        "address": "Cl 80 #32-10, Salitre",
        "rate_car_per_hour": 5500,
        "rate_moto_per_hour": 2800,
        "rating": 4.0,
        "reviews": []
    }
]

# -------------------------
# Utilidades: recalcular calificación
# -------------------------
def recalc_rating(p):
    if not p["reviews"]:
        p["rating"] = 0.0
        return
    avg = sum(r["stars"] for r in p["reviews"]) / len(p["reviews"])
    p["rating"] = round(avg, 2)

for p in parkings:
    recalc_rating(p)

# -------------------------
# Ventanas / App
# -------------------------
class SmartTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartTrack Parking - Prototipo")
        self.root.geometry("360x640")  # tamaño tipo móvil vertical
        self.root.resizable(False, False)
        self.logo_img = None
        self.load_logo()

        # Inicial: mostrar splash
        self.show_splash()

    def load_logo(self):
        try:
            img = Image.open("logo-proyecto.png")
            # redimensionar manteniendo aspecto (ancho 220)
            w = 220
            ratio = w / img.width
            h = int(img.height * ratio)
            img = img.resize((w, h), Image.ANTIALIAS)
            self.logo_img = ImageTk.PhotoImage(img)
        except Exception as e:
            print("No se pudo cargar logo-proyecto.png:", e)
            self.logo_img = None

    # -------------------------
    # Pantalla de inicio (Splash)
    # -------------------------
    def show_splash(self):
        self.clear_root()
        frame = Frame(self.root, bg="#FFFFFF")
        frame.pack(fill="both", expand=True)

        # logo
        if self.logo_img:
            lbl_logo = Label(frame, image=self.logo_img, bg="#FFFFFF")
            lbl_logo.pack(pady=(40,10))
        else:
            lbl_logo = Label(frame, text="SmartTrack Parking", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#1976D2")
            lbl_logo.pack(pady=(60,10))

        subtitle = Label(frame, text="Encuentra parqueaderos en Bogotá", bg="#FFFFFF", fg="#1976D2", font=("Helvetica", 10))
        subtitle.pack(pady=(0,20))

        btn_enter = Button(frame, text="Entrar", command=self.show_main_window, bg="#4DB6AC", fg="white",
                           font=("Helvetica", 12, "bold"), bd=0, relief="ridge", padx=20, pady=8)
        btn_enter.pack(pady=10)

        # pequeño pie
        lbl_foot = Label(frame, text="Prototipo - Presentación", bg="#FFFFFF", fg="#6E6E6E", font=("Helvetica", 8))
        lbl_foot.pack(side="bottom", pady=12)

    # -------------------------
    # Ventana principal: lista de parqueaderos
    # -------------------------
    def show_main_window(self):
        self.clear_root()
        container = Frame(self.root, bg="#FFFFFF")
        container.pack(fill="both", expand=True)

        # Encabezado con logo y título (si existe)
        header = Frame(container, bg="#FFFFFF")
        header.pack(fill="x", pady=8, padx=8)
        if self.logo_img:
            logo_small = self.logo_img  # ya es pequeño
            Label(header, image=logo_small, bg="#FFFFFF").pack(side="left", padx=(0,8))
        Label(header, text="SmartTrack Parking", bg="#FFFFFF", fg="#1976D2", font=("Helvetica", 14, "bold")).pack(side="left")

        # Búsqueda/Filtro (simulado): desplegable para filtrar por nombre (o All)
        search_frame = Frame(container, bg="#FFFFFF")
        search_frame.pack(fill="x", padx=12, pady=(6,6))

        Label(search_frame, text="Filtrar por proveedor:", bg="#FFFFFF", fg="#333", font=("Helvetica", 9)).pack(anchor="w")
        providers = ["Todos", "City Parking", "GeoParking", "Centros Comerciales", "Otros"]
        self.filter_var = StringVar(value="Todos")
        cb = ttk.Combobox(search_frame, values=providers, state="readonly", textvariable=self.filter_var)
        cb.pack(fill="x", pady=4)

        # Lista (Frame con scroll)
        list_frame = Frame(container, bg="#F7F9FB", bd=0)
        list_frame.pack(fill="both", expand=True, padx=12, pady=(6,10))

        canvas = Canvas(list_frame, bg="#F7F9FB", highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
        scrollable = Frame(canvas, bg="#F7F9FB")

        scrollable.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # llenar la lista
        for p in parkings:
            self._add_parking_card(scrollable, p)

    def _add_parking_card(self, parent, p):
        card = Frame(parent, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="x", pady=8, padx=6)

        top = Frame(card, bg="white")
        top.pack(fill="x", padx=8, pady=8)
        Label(top, text=p["name"], bg="white", fg="#1976D2", font=("Helvetica", 11, "bold")).pack(anchor="w")
        Label(top, text=p["address"], bg="white", fg="#555", font=("Helvetica", 9)).pack(anchor="w", pady=(2,0))

        info = Frame(card, bg="white")
        info.pack(fill="x", padx=8, pady=(4,8))

        left = Frame(info, bg="white")
        left.pack(side="left", anchor="w")
        Label(left, text=f"${p['rate_car_per_hour']}/h (auto)", bg="white", fg="#000", font=("Helvetica", 9)).pack(anchor="w")
        Label(left, text=f"Calificación: {p['rating']}", bg="white", fg="#000", font=("Helvetica", 9)).pack(anchor="w", pady=(2,0))

        btn = Button(info, text="Ver detalles", bg="#4DB6AC", fg="white", bd=0, padx=10,
                     command=lambda pk=p: self.open_details(pk))
        btn.pack(side="right", padx=8)

    # -------------------------
    # Ventana detalles
    # -------------------------
    def open_details(self, parking):
        top = Toplevel(self.root)
        top.title(parking["name"])
        top.geometry("360x520")
        top.resizable(False, False)
        top.configure(bg="#FFFFFF")

        # Encabezado con logo y nombre
        if self.logo_img:
            header = Frame(top, bg="#FFFFFF")
            header.pack(fill="x", pady=8)
            Label(header, image=self.logo_img, bg="#FFFFFF").pack(side="left", padx=6)
            Label(header, text=parking["name"], bg="#FFFFFF", fg="#1976D2", font=("Helvetica", 12, "bold")).pack(side="left", padx=6)

        content = Frame(top, bg="#FFFFFF")
        content.pack(fill="both", expand=True, padx=12, pady=8)

        Label(content, text="Dirección:", bg="#FFFFFF", fg="#333", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(6,0))
        Label(content, text=parking["address"], bg="#FFFFFF", fg="#555", font=("Helvetica", 10)).pack(anchor="w")

        Label(content, text="Tarifas:", bg="#FFFFFF", fg="#333", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(8,0))
        Label(content, text=f"Auto: ${parking['rate_car_per_hour']} / h", bg="#FFFFFF", fg="#555", font=("Helvetica", 10)).pack(anchor="w")
        Label(content, text=f"Moto: ${parking['rate_moto_per_hour']} / h", bg="#FFFFFF", fg="#555", font=("Helvetica", 10)).pack(anchor="w")

        Label(content, text="Disponibilidad (simulada):", bg="#FFFFFF", fg="#333", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(8,0))
        # Simulación simple (aleatoria por ahora: determinista)
        available_text = "Alta disponibilidad" if parking["rating"] >= 4.0 else "Media / Limitada"
        Label(content, text=available_text, bg="#FFFFFF", fg="#555", font=("Helvetica", 10)).pack(anchor="w")

        Label(content, text="Calificación promedio:", bg="#FFFFFF", fg="#333", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(8,0))
        Label(content, text=f"{parking['rating']} ⭐", bg="#FFFFFF", fg="#555", font=("Helvetica", 10)).pack(anchor="w")

        # Botones
        btn_frame = Frame(content, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=18)
        Button(btn_frame, text="Dejar reseña", bg="#1976D2", fg="white", bd=0, padx=10,
               command=lambda pk=parking, t=top: self.open_review_window(pk, t)).pack(side="left", padx=6)
        Button(btn_frame, text="Cerrar", bg="#B0BEC5", fg="white", bd=0, padx=10,
               command=top.destroy).pack(side="right", padx=6)

    # -------------------------
    # Ventana de encuesta / reseña
    # -------------------------
    def open_review_window(self, parking, parent_window=None):
        # Esta ventana no mostrará el logo (solicitud del usuario para limpieza)
        rv = Toplevel(self.root)
        rv.title("Dejar reseña - " + parking["name"])
        rv.geometry("340x420")
        rv.resizable(False, False)
        rv.configure(bg="#FFFFFF")

        frame = Frame(rv, bg="#FFFFFF", padx=12, pady=12)
        frame.pack(fill="both", expand=True)

        Label(frame, text="Califica tu experiencia (1-5):", bg="#FFFFFF", fg="#333", font=("Helvetica", 10)).pack(anchor="w")
        star_var = IntVar(value=5)
        stars_frame = Frame(frame, bg="#FFFFFF")
        stars_frame.pack(anchor="w", pady=(4,10))
        for i in range(1,6):
            r = Radiobutton(stars_frame, text=str(i), variable=star_var, value=i, bg="#FFFFFF")
            r.pack(side="left", padx=4)

        Label(frame, text="Comentario (opcional):", bg="#FFFFFF", fg="#333", font=("Helvetica", 10)).pack(anchor="w")
        txt = Text(frame, height=8, width=36, bd=1, relief="solid")
        txt.pack(pady=(6,10))

        def send_review():
            stars = star_var.get()
            comment = txt.get("1.0", "end").strip()
            parking["reviews"].append({"stars": stars, "text": comment})
            recalc_rating(parking)
            messagebox.showinfo("¡Gracias!", "Tu reseña fue enviada. Calificación actual: " + str(parking["rating"]))
            rv.destroy()
            # opcional: refrescar la ventana principal (simple: re-open main)
            self.show_main_window()
            if parent_window:
                try:
                    parent_window.lift()
                except:
                    pass

        Button(frame, text="Enviar", bg="#4DB6AC", fg="white", bd=0, padx=10, command=send_review).pack(side="left", pady=6, padx=6)
        Button(frame, text="Cancelar", bg="#B0BEC5", fg="white", bd=0, padx=10, command=rv.destroy).pack(side="right", pady=6, padx=6)

    # -------------------------
    # Helpers
    # -------------------------
    def clear_root(self):
        for w in self.root.winfo_children():
            w.destroy()

# -------------------------
# Ejecutar app
# -------------------------
if __name__ == "__main__":
    root = Tk()
    app = SmartTrackApp(root)
    root.mainloop()