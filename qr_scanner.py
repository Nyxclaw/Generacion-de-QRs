import qrcode

# 1. Colocar enlace directo
enlace_formulario = "https://docs.google.com/forms/d/e/TU_ENLACE_AQUI/viewform"

# 2. Configurar el diseño del QR (esto es opcional, pero le da mejor calidad)
qr = qrcode.QRCode(
    version=1, # Tamaño del QR (del 1 al 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta resistencia a daños (hasta 30%)
    box_size=10, # Tamaño de cada cuadrito
    border=4, # Grosor del borde blanco
)

# 3. Agregar los datos y generar la matriz
qr.add_data(enlace_formulario)
qr.make(fit=True)

# 4. Crear la imagen final y guardar en local
imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save("QR_Scan.png")

print("¡Listo! Tu código QR estático se ha generado con éxito.")