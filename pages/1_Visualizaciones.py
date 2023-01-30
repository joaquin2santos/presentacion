import streamlit as st

st.title("Visualizaciones")
tab1, tab2, tab3 = st.tabs(["Tiempo de Entrega", "Satisfaccion del Cliente", "Ventas por Producto"])

with tab1:
    st.title("Disminuir tiempos de Entrega")
    st.subheader("KPI:")
    #st.markdown("***")
    st.subheader(""" Reducir los tiempos de entrega 5% semestral.""")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/imagen2.png?raw=true")
    st.write("""En el primer grafico de arriba a la izquierda(Velocimetro) podemos observar el promedio nacional
           que demora todo proceso desde que el cliente compra el producto, hasta que le es entregado. A su lado se
           encuentra el promedio nacional de tiempos de entrega estimados, ambas medidas estan en dias""")

    st.write("""El grafico titulado 'Diferencia Porcentual' en la parte superior muestra el porcentaje de diferencia entre el
     que estimado y el tiempo real que tenemos para las entregas.""")

    st.write("""En el tercer grafico  de la parte superior muestra el promedio nacional en el que el vendedor despacha 
        el producto vendido. Cabe destacar que esta parte del proceso no depende de Olist pero decidimos incluirla
        porque influye de sobremanera en el resultado del proceso final.""")
    st.write("""En el cuarto grafico de la parte superior se encuentra el promedio nacional de entrega al cliente, 
    una vez que el producto esta en manos de Olist. Es decir, esta parte depende pura y exclusivamente de la empresa""")

    st.write("""En el mapa podemos ver el promedio de entrega en dias por estado. Entendemos que brasil tiene una geografia 
            particular por lo que creemos necesario hacer esta distincion por zona.""")
    st.write("""A la derecha del mapa, podemos observar el promedio de tiempo de entrega en dias agrupado por region y/o distrito""")

    st.write("""En la esquina inferior derecha podemos observar la cantidad de ordenes por cada estado del pais""")
with tab2:
    st.title("Satisfaccion del cliente en relacion a tiempos de entrega")
    st.subheader("KPI:")
    st.subheader("""Aumentar en 2% semestral por 3 años las reviews positivas""")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/imagen1.png?raw=true")
    st.write("""En el mapa ubicado en la parte superior izquierda podemos ver el promedio de scores de reseñas discriminado
        por region""")
    st.write("""En el grafico de velocimetro ubicado a su derecha podemos ver el promedio de score de reseñas nacional.""")
    st.write("""En la tabla que se encuentra a la derecha del grafico velocimetro, encontramos el porcentaje de reseñas
            que pertenece a cada puntaje de score""")
    st.write("""En la parte inferior izquierda podemos encontrar la evolucion de los scores de reseñas a lo largo del tiempo""")
    st.write("""A su derecha podemos ver el total acumulado por cada puntaje del score de reseñas""")

with tab3:
    st.title("Distribucion de Ventas por Categoria de Productos")
    st.subheader("KPI:")
    st.subheader("Aumentar la cantidad de productos vendidos en un 15% anual")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/imagen3.png?raw=true")
    st.write("""En el grafico de la parte superior izquierda tenemos el acumulado de ventas separado por categoria de productos""")
    st.write("""En la tajeta a su derecha tenemos el acumulado total de ventas para el periodo seleccionado""")
    st.write("""Por ultimo en la parte inferior econtramos la evolucion en el tiempo de la cantidad de ventas de la plataforma de Olist""")
    