import streamlit as st
import pandas as pd
import time


st.set_page_config(page_title="Hello World", page_icon="🧊")


st.title("Hello World")
st.header("This is a header")
st.subheader("This is a subheader")
""
st.markdown("# This is a markdown")

st.markdown("---")

st.success("Exitoso!!✅")
st.info("Información")
st.warning("Advertencia")
st.error("Error")


st.write("This is a write")

st.markdown("# Elementos dinamicos")

seleccion = st.checkbox("Checkbox")
print(seleccion)
radio_seleccion = st.radio("Radio", ("Option 1", "Option 2", "Option 3"))
print(radio_seleccion)
st.button("Button")
var = st.selectbox("Selectbox", ("Option 1", "Option 2", "Option 3"))
st.markdown("---")

st.file_uploader("File uploader")

st.success("ud selecciono: "+var)
st.sidebar.title("Esta es la barra lateral")
st.sidebar.radio("Radio2", ("Option 1", "Option 2", "Option 3"))



st.sidebar.file_uploader("File uploader2")

st.markdown("---")

col1,col2 = st.columns(2) # (col1,col2,...coln)

with col1:
    st.write("Columna 1")
    st.write("Columna 1")
    st.button("Button2")
    st.slider("Sliderx", 0, 100)
with col2:
    st.write("Columna 2")
    data = {"data": [1,2,3,4,5,6,7,8,9,10]}
    df = pd.DataFrame(data)
    st.dataframe(df)


st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

latest_iteration = st.empty()
bar = st.progress(0)

st.markdown("---")

# Carguemos los datos del titanic para probar el uso de los elementos.
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
st.dataframe(df)

columnas = df.columns

columna_interes = st.selectbox("Columnas", columnas)



counts = df[columna_interes].value_counts()
import matplotlib.pyplot as plt

# Crear el gráfico de torta con Matplotlib
fig, ax = plt.subplots()
ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Para que el gráfico sea un círculo perfecto

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
# ...