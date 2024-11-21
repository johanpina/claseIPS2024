import streamlit as st

st.title('Hola mundo 👋')
st.write('Esta es mi primera aplicacion')


st.markdown("---")

st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3]) # list, numpy, pandas, dict

st.text("Fixed width text")
st.markdown("_Markdown_")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>") 

st.markdown("---")

import pandas as pd

my_dataframe = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/nba-player-stats-2019.csv")

st.dataframe(my_dataframe)
st.table(my_dataframe.iloc[0:10])

st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, -2)

st.markdown("---")

st.image("./25231.png")

st.markdown("---")

st.sidebar.title("Esta es una barra lateral 📏")

# Just add it after st.sidebar:
a = st.sidebar.radio("Select one:", [1, 2])

# Or use "with" notation:
with st.sidebar:
    mi_respuesta = st.radio("esta es mi seccion radio :", [1, 2,22,33,44,])
    print(mi_respuesta)

st.markdown("---")

st.selectbox("Select box", [1, 2, 3])  



