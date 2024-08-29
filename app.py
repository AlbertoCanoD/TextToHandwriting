import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Configurar el tema de la aplicación
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Función para cargar la fuente manuscrita similar a la de pywhatkit
def cargar_fuente():
    try:
        return ImageFont.truetype("DancingScript-Regular.ttf", 40)
    except IOError:
        messagebox.showerror("Error", "No se pudo cargar la fuente manuscrita. Asegúrate de que el archivo esté en la misma carpeta.")
        return None


# Cargar la fuente manuscrita
fuente_manuscrita = cargar_fuente()


# Función para actualizar el preview de la imagen
def actualizar_preview():
    texto = entry_texto.get("1.0", "end-1c")
    if not texto.strip():
        texto = "Texto de ejemplo"

    try:
        img = Image.new("RGB", (400, 300), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        if fuente_manuscrita:
            draw.text((50, 120), texto, fill=(colorR, colorG, colorB), font=fuente_manuscrita)

        img_tk = ImageTk.PhotoImage(img)
        label_imagen.configure(image=img_tk)
        label_imagen.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al generar la vista previa: {e}")


# Función personalizada para seleccionar un color integrado en la interfaz principal
def seleccionar_color():
    global colorR, colorG, colorB, slider_rojo, slider_verde, slider_azul, color_frame

    def actualizar_color(value=None):
        global colorR, colorG, colorB
        colorR = int(slider_rojo.get())
        colorG = int(slider_verde.get())
        colorB = int(slider_azul.get())
        color_frame.configure(fg_color=f'#{colorR:02x}{colorG:02x}{colorB:02x}')
        actualizar_preview()

    # Crear un frame para contener los sliders de color
    color_frame_container = ctk.CTkFrame(frame)
    color_frame_container.grid(row=5, column=0, sticky="ew", padx=20, pady=10)
    color_frame_container.grid_columnconfigure(1, weight=1)  # Permitir que la columna de los sliders se expanda

    # Sliders para seleccionar el color
    slider_rojo = ctk.CTkSlider(color_frame_container, from_=0, to=255, command=actualizar_color)
    slider_rojo.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
    slider_verde = ctk.CTkSlider(color_frame_container, from_=0, to=255, command=actualizar_color)
    slider_verde.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
    slider_azul = ctk.CTkSlider(color_frame_container, from_=0, to=255, command=actualizar_color)
    slider_azul.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    # Etiquetas para cada color
    label_rojo = ctk.CTkLabel(color_frame_container, text="Rojo")
    label_rojo.grid(row=0, column=0, padx=10, pady=5)
    label_verde = ctk.CTkLabel(color_frame_container, text="Verde")
    label_verde.grid(row=1, column=0, padx=10, pady=5)
    label_azul = ctk.CTkLabel(color_frame_container, text="Azul")
    label_azul.grid(row=2, column=0, padx=10, pady=5)

    # Frame para mostrar el color seleccionado, posicionado a la derecha de los sliders
    color_frame = ctk.CTkFrame(color_frame_container, width=100, height=100)
    color_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=5)

    # Iniciar los sliders con los valores actuales de color
    slider_rojo.set(colorR)
    slider_verde.set(colorG)
    slider_azul.set(colorB)
    actualizar_color()


# Función para transcribir el texto a imagen
def transcribir_texto():
    texto = entry_texto.get("1.0", "end-1c")
    st = entry_titulo.get() + ".png"

    try:
        if any(c < 0 or c > 255 for c in [colorR, colorG, colorB]):
            raise ValueError("Los valores RGB deben estar entre 0 y 255")

        img = Image.new("RGB", (400, 300), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        if fuente_manuscrita:
            draw.text((50, 120), texto, fill=(colorR, colorG, colorB), font=fuente_manuscrita)

        img.save(st)
        messagebox.showinfo("Éxito", f"Imagen '{st}' creada con éxito!")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al crear la imagen: {e}")


# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Transcribir Texto a Imagen")
ventana.geometry("500x700")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

# Variables para los colores
colorR, colorG, colorB = 0, 0, 0

# Crear widgets
frame = ctk.CTkFrame(ventana)
frame.grid(sticky="nsew", padx=20, pady=20)
frame.grid_columnconfigure(0, weight=1)

label_texto = ctk.CTkLabel(frame, text="Introduzca el texto:")
label_texto.grid(row=0, column=0, sticky="w", pady=10)

entry_texto = ctk.CTkTextbox(frame, height=150, width=400)
entry_texto.grid(row=1, column=0, sticky="nsew", pady=10)

label_titulo = ctk.CTkLabel(frame, text="Introduzca el título de la imagen:")
label_titulo.grid(row=2, column=0, sticky="w", pady=10)

entry_titulo = ctk.CTkEntry(frame)
entry_titulo.grid(row=3, column=0, sticky="ew", pady=10)

label_color = ctk.CTkLabel(frame, text="Seleccione el color del texto:")
label_color.grid(row=4, column=0, sticky="w", pady=10)

# Definir label_imagen antes de la primera llamada a actualizar_preview
label_imagen = ctk.CTkLabel(frame, text="")
label_imagen.grid(row=7, column=0, sticky="nsew", pady=10)

# Llamar directamente al selector de color personalizado
seleccionar_color()

label_preview = ctk.CTkLabel(frame, text="Preview de la imagen:")
label_preview.grid(row=6, column=0, sticky="w", pady=10)

boton_transcribir = ctk.CTkButton(frame, text="Crear Imagen", command=transcribir_texto)
boton_transcribir.grid(row=8, column=0, sticky="ew", pady=20)

frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(7, weight=1)

entry_texto.bind("<KeyRelease>", lambda event: actualizar_preview())

actualizar_preview()

ventana.mainloop()
