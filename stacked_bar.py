import streamlit as st
import pandas as pd
import altair as alt

# Dados de exemplo
data = pd.DataFrame({
    "Categoria": ["A", "A", "B", "B", "C", "C"],
    "Grupo": ["X", "Y", "X", "Y", "X", "Y"],
    "Valor": [3, 2, 4, 1, 5, 3]
})

# Gráfico stacked
chart = alt.Chart(data).mark_bar().encode(
    x="Categoria:N",
    y="Valor:Q",
    color="Grupo:N"
).properties(width=600)

st.altair_chart(chart, use_container_width=True)