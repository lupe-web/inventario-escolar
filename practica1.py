import streamlit as st
st.titlle("Mi primera aplicacion")
nombre=st.text_input("Escribe tu nombre")
apellido=st.text_input("Escribe tu apellido")
if nombre and apellido:
    st.success(f"Bienvenido {nombre} " f" {apellido}")