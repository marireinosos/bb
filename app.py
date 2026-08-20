import streamlit as st
from PIL import Image

st.title ("Mi primera App!!")

st.header ("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write ("facilmete puedo realiza beckend y frontend.")
image = Image.open('Interfaces lanaDelRey.jpg')
st.image (image, caption = 'Interfaces multimodales')
