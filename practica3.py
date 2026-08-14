import streamlit as st 
st.title("Calcular el descuento")
producto=st.text_input("Escribe el producto")
precio=st.number_input("Escribe el precio", min_value=0)
if st.button ("Calcular total"):
    if precio>= 50:
        descuento= precio=0.20
    else:
        descuento=0
        total=precio-descuento

        st.write("Producto", producto)
        st.write("Precio inicial", precio)
        st.write("Descuento", descuento)
        st.write("Total a pagar", total)