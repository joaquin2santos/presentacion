import streamlit as st

st.title("Esquema de Trabajo")

st.markdown("Este proyecto lo realizamos de la siguiente manera:")

st.subheader("Nuestro Repo")
st.markdown("https://github.com/lulo76/Proyecto-Final-DTS--05")


tab1, tab2, tab3, tab4 = st.tabs(["Nuestro Team", "Diagrama de Gantt", "Workflow", "Metodologias"])

with tab1:
    st.subheader("Nuestro team")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Assets/dev%20team%20olist.png?raw=true")

with tab2:
    st.subheader("Utilizamos el siguiente diagrama de Gant:")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Assets/diagrama_gantt03.png?raw=true")

with tab3: 
    st.subheader("El Workflow de trabajo se estructuro de la siguiente manera")
    st.markdown("Etapa Local")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Assets/workflowlocal.png?raw=true")
    st.write("""En esta etapa buscamos manejar los archivos de forma local, realizando un analisis EDA y pasos 
            preliminares para entender que necesitamos para el proyecto""")
    st.markdown("***")
    st.markdown("Escalabilidad")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Assets/workflowairflow.png?raw=true")
    st.write("""En este segundo momento intentamos escalar el flujo de datos hasta hacerlo automatizado, mediante
            tecnologias como Airflow que nos ahorran tiempo en los procesos.""")
    st.markdown("***")
    st.subheader("Utilizamos el gestor de proyecto trello")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Assets/trello.png?raw=true")
    st.write("""Para coordinar las tareas del dia a dia utilizamos esta herramienta, asi cada integrante del equipo 
            puede reportar en que se encuentra trabajando y a su vez saber como esta el avance sus compañeros.""")
with tab4: 
    st.subheader("Metodologia Agile-Scrum")
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Assets/metodologia.png?raw=true")
    st.write("""Metodología de trabajo.
        La metodología de gestión de proyecto utilizada se cree muy importante para llegar a los
        objetivos propuestos. Se utilizará metodología considerada ágil al ser colaborativa, rápida
        y efectiva, iterativa, respaldada por datos y fundamentalmente que se valore a las personas}
        por encima de los procesos ya que se deduce que es la mejor y más eficiente manera de trabajo.
        En particular se realizará la metodología Scrum, que se basa en “Sprints” para crear un ciclo 
        de proyecto, en este caso, sprints de una semana. Cada sprint culminará con la demostración del
        progreso del trabajo realizado hasta el momento, frente al Product Owner. La duración total del 
        proyecto será de 4 semanas. Siendo la última exclusivamente para presentación final y demostrar 
        puesta en producción. Se realizan reuniones diarias (guiadas por un Scrum Master) con el objetivo
        de conocer a todos los participantes del proyecto, dividiendo, organizando trabajo y tiempos por 
        cada integrante y así garantizar que las tareas se finalicen a tiempo y de manera correcta.""")