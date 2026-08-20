import streamlit as st
from PIL import Image
import os

st.title("¡Mi primera App!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend.")

image_path = 'lanaDelRey.jpg'


if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption='Interfaces multimodales')
else:
    # Mensaje de error amigable por si la imagen no carga
    st.error(f"No se pudo encontrar la imagen: {image_path}")
    st.warning("Recuerda verificar que el archivo 'lanaDelRey.jpg' esté subido en tu repositorio de GitHub en la misma carpeta que este código.")

texto = st.text_input('Escribe algo', 'Este es mi texto')


st.write('El tedxto escrito es', texto)
st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
    # 1. Corregido: Se agregó el punto (st.subheader)
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    
    # 2. Corregido: La indentación (los espacios) están alineados correctamente
    if resp:
        st.write('¡Correcto!')

with col2:
    st.subheader ("Esta es la segunda columna")
    modo = st.radio ("Que Modalidad es la principal es tu interfaz", ('Visual', auditiva', 'Tactil'))
        if modo =='Visual':
        st.write ('La vista es fundamental para tu interfaz')
        if modo == áuditiva':
        st.write ('La audicion es fundamental para tu interfaz´)
        if modo == 'Tactil':
                  st.write ('El tacto es fundamental para tu interfaz')
