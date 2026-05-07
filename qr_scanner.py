import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import ImageTk, Image

def generar_y_guardar():
    url = entrada_url.get()
    
    if not url:
        messagebox.showwarning("Error", "Por favor, introduce un enlace de Google Forms.")
        return

    # Preguntar al usuario dónde quiere guardar el archivo
    ruta_archivo = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Archivo PNG", "*.png")],
        title="Guardar código QR como..."
    )

    if ruta_archivo:
        try:
            # Configuración del QR
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(ruta_archivo)
            
            messagebox.showinfo("Éxito", f"QR guardado correctamente en:\n{ruta_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el QR: {e}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de QR Eternos - Nyxclaw")
ventana.geometry("400x250")
ventana.resizable(False, False)

# Elementos de la interfaz
label_instruccion = tk.Label(ventana, text="Pega el enlace de tu formulario aquí:", font=("Arial", 10))
label_instruccion.pack(pady=20)

entrada_url = tk.Entry(ventana, width=50)
entrada_url.pack(pady=5)
entrada_url.focus_set()

boton_generar = tk.Button(ventana, text="Generar y Descargar QR", 
                          command=generar_y_guardar, 
                          bg="#4CAF50", fg="white", 
                          font=("Arial", 10, "bold"),
                          padx=10, pady=5)
boton_generar.pack(pady=30)

ventana.mainloop()
