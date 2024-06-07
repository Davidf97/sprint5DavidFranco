import streamlit as st
import pandas as pd 
import plotly_express as px

car_data= pd.read_csv('vehicles_us.csv')
hist_button= st.button ('Construir histograma')
disp_button= st.button ('Construir diagrama de dispersión')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig= px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True) #falta agregar otro botton para dispersion


elif disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches') 
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True) 

