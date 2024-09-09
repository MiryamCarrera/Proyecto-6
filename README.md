# Proyecto-6
Este es un repositorio para el proyecto 6 de Tripleten
En este proyecto del sprint 6 nos permite analizar la base de datos vehicles_us con el objetivo de generar un histograma y un diagrama de dispersion con el objetivo de visualizar los datos y su comportamiento. por lo que generamos dos casillas sustiituyendo a los botones para que el usario que tenga acceso al sitio pueda elegir cual desplegar y visualizar los datos.
En el proyecto se trabajo con las librerias pandas, streamlit y plotly-express, se genraron los folders de python, texto necesarios para que el programa corriera correctamente.
Las casillas de verificación (st.checkbox): Permiten al usuario seleccionar si desea ver el histograma o el gráfico de dispersión (o ambos).
Si la casilla de verificación está marcada, se generará el gráfico correspondiente.
Para realizar el programa usamos st.write() para mostrar mensajes sobre qué gráfico se está creando y st.plotly_chart() para mostrar el gráfico interactivo.
Al hacer clic en la casilla, se muestra un gráfico de dispersión (scatter plot) que visualiza la relación entre el odometer (kilometraje) y el price (precio) de los vehículos, coloreado por el año de fabricación (year).
Se utilizan las funciones st.write() para mostrar mensajes y st.plotly_chart() para renderizar ambos gráficos.
Por ultimo ralizamos los ajustes en la terminal de git para correr, guardar cambios con las anotaciones (git commit -m), y al final enviarlo a github (git push).
