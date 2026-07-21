import streamlit as st

# Inicializar inventario
if "productos" not in st.session_state:
    st.session_state.productos = []

st.title("📚 Sistema de Inventario Escolar")

st.header("Registrar Producto")

nombre = st.text_input("Nombre del producto")

precio = st.number_input(
    "Precio ($)",
    min_value=0.0,
    format="%.2f"
)

cantidad = st.number_input(
    "Cantidad",
    min_value=0,
    step=1
)

if st.button("Registrar Producto"):
    if nombre:
        total = precio * cantidad

        st.session_state.productos.append({
            "Producto": nombre,
            "Precio": precio,
            "Cantidad": cantidad,
            "Total": total
        })

        st.success(f"✅ {nombre} registrado correctamente")
    else:
        st.error("⚠️ Debes ingresar un nombre de producto")

st.header("Inventario Actual")

if st.session_state.productos:
    gran_total = 0

    for producto in st.session_state.productos:
        gran_total += producto["Total"]

    st.table(st.session_state.productos)

    st.subheader(f"💰 Valor total del inventario: ${gran_total:.2f}")

else:
    st.info("El inventario está vacío.")