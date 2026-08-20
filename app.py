import streamlit as st
from PIL import Image
import os

st.title("¡Mi primera App!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend.")

# Aquí ponemos el nombre exacto de tu imagen
image_path = 'lanaDelRey.jpg'

# Verificamos si la imagen existe para evitar que la app se caiga
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption='Interfaces multimodales')
else:
    # Mensaje de error amigable por si la imagen no carga
    st.error(f"No se pudo encontrar la imagen: {image_path}")
    st.warning("Recuerda verificar que el archivo 'lanaDelRey.jpg' esté subido en tu repositorio de GitHub en la misma carpeta que este código.")
# 1. Corregido: text_input con "n"
texto = st.text_input('Escribe algo', 'Este es mi texto')

# 2. Corregido: st.write en minúsculas y separamos el texto de la variable
st.write('El tedxto escrito es', texto)
