import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

st.sidebar.title("ACTIVIDADES")
opciones = st.sidebar.radio("primero cargue sus datos", ["datos", "inicio", "Ayuda"])

if opciones == "datos":
   st.title("INGRESO DE DATOS")
    
   if "messages" not in st.session_state:
    st.session_state.messages = []

    for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.markdown(message["content"])

   user_tipoDeDiabetes = st.text_input("que tipo de diabetes tiene?:")
   user_infoMedica = st.text_input("¿Hay alguna otra condición médica relevante además de la diabetes?:")
   user_edad = st.text_input("qu edad tiene?:")
   user_genero = st.text_input("que genero es?:")
   user_peso = st.text_input("su peso:")
   user_estatura = st.text_input("altura:")
   user_actividad= st.text_input("cuanto ejercicio realiza regularmente?")
   user_objetivos = st.text_input("esta buscando perder peso ,mantenerlo o ganar peso?:")
   user_medicamentos = st.text_input("esta tomando medicamento para controlar la diabetes?:")

   if user_tipoDeDiabetes and user_peso and user_actividad and user_edad and user_estatura and user_genero and user_infoMedica and user_medicamentos and user_objetivos:
    prompt = f'Con los siguientes datos proporcionados, por favor, genere un plan nutricional para una persona con diabetes: Tipo de diabetes: {user_tipoDeDiabetes} , Información médica relevante: {user_infoMedica}, Edad y género: {user_edad},{user_genero} , Peso corporal (kg) y estatura (cm): {user_peso},{user_estatura} , Nivel de actividad física: {user_actividad} , Objetivos de salud (perder, mantener o ganar peso): {user_objetivos} , Medicamentos actuales: {user_medicamentos}. El plan debe incluir recomendaciones dietéticas específicas, el número de comidas por día, porciones sugeridas, y pautas para el control de carbohidratos y azúcar. Por favor, proporcione detalles precisos para ayudar a la persona con diabetes a gestionar su condición de manera efectiva'
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
elif opciones == "inicio":
     st.write("Configura tu aplicación aquí.")
   
elif opciones == "Ayuda":

    st.write("¿Necesitas ayuda?")  
    st.write("¿preguntas?")  