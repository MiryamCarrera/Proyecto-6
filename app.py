import pandas as pd
import streamlit as st
import plotly.express as px

datos= pd.read_csv('./vehicles_us.csv')

#print(datos.head())

# Crear casillas de verificación para histograma
mostrar_histograma = st.checkbox('Mostrar histograma')

# Crear casillas de verificación para dispersion
mostrar_dispersion = st.checkbox('Mostrar gráfico de dispersión')

# Si se selecciona la casilla de verificación del histograma
if mostrar_histograma:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig_hist = px.histogram(datos, x="odometer")
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Si se selecciona la casilla de verificación del gráfico de dispersión
if mostrar_dispersion:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    fig_dispersion = px.scatter(datos, x="odometer", y="price", color="model_year", title="Relación entre odometer y precio")
    
    st.plotly_chart(fig_dispersion, use_container_width=True)
