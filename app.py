import openai
import streamlit as st

# Configuración de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

st.sidebar.title("barra de opciones")
opciones = st.sidebar.radio("Seleccione una actividad", ["inicio","Carga de Datos", "Plan Nutricional", "Ayuda"])
if opciones == "inicio":
    control=False

if opciones == "Carga de Datos":
    st.title("CARGA DE DATOS")

    # Inicializar o cargar datos del usuario
    user_data = st.session_state.get("user_data", {
        "Tipo de diabetes": "",
        "Información médica": "",
        "Edad": "",
        "Género": "",
        "Peso": "",
        "Estatura": "",
        "Actividad física": "",
        "Objetivos de salud": "",
        "Medicamentos": ""
    })

    # Formulario para ingresar datos
    user_tipoDeDiabetes = st.text_input("¿Qué tipo de diabetes tiene?", user_data["Tipo de diabetes"])
    user_infoMedica = st.text_input("¿Hay alguna otra condición médica relevante además de la diabetes?", user_data["Información médica"])
    user_edad = st.text_input("¿Qué edad tiene?", user_data["Edad"])
    user_genero = st.text_input("¿Qué género es?", user_data["Género"])
    user_peso = st.text_input("Su peso:", user_data["Peso"])
    user_estatura = st.text_input("Altura:", user_data["Estatura"])
    user_actividad = st.text_input("¿Cuánto ejercicio realiza regularmente?", user_data["Actividad física"])
    user_objetivos = st.text_input("¿Está buscando perder peso, mantenerlo o ganar peso?", user_data["Objetivos de salud"])
    user_medicamentos = st.text_input("¿Está tomando medicamento para controlar la diabetes?", user_data["Medicamentos"])

    if st.button("Guardar Datos"):
        campos_obligatorios = [user_tipoDeDiabetes, user_edad, user_genero, user_peso, user_estatura, user_actividad, user_objetivos]
        if all(campos_obligatorios):
        # Guardar datos en session_state
            user_data = {
             "Tipo de diabetes": user_tipoDeDiabetes,
             "Información médica": user_infoMedica,
             "Edad": user_edad,
             "Género": user_genero,
             "Peso": user_peso,
             "Estatura": user_estatura,
             "Actividad física": user_actividad,
             "Objetivos de salud": user_objetivos,
             "Medicamentos": user_medicamentos,
             }
            st.session_state.user_data = user_data
            st.success("Datos guardados correctamente.")
        else:
         st.warning("Por favor, complete todos los campos obligatorios.")


if opciones == "Plan Nutricional":
    st.title("NutriGod")
    st.subheader("Plan nutricional")
    

    # Verificar si los datos están cargados
    if "user_data" not in st.session_state:
        st.warning("Por favor, cargue los datos en la opción 'Carga de Datos' primero.")
    else:
        user_data = st.session_state.user_data

        # Crear el prompt con los datos cargados
        prompt = f'Con los siguientes datos proporcionados, por favor, genere un plan nutricional para una persona con diabetes:\n\nTipo de diabetes: {user_data["Tipo de diabetes"]}\nInformación médica relevante: {user_data["Información médica"]}\nEdad y género: {user_data["Edad"]}, {user_data["Género"]}\nPeso corporal (kg) y estatura (cm): {user_data["Peso"]}, {user_data["Estatura"]}\nNivel de actividad física: {user_data["Actividad física"]}\nObjetivos de salud (perder, mantener o ganar peso): {user_data["Objetivos de salud"]}\nMedicamentos actuales: {user_data["Medicamentos"]}\n\nEl plan debe incluir recomendaciones dietéticas específicas, el número de comidas por día, porciones sugeridas y pautas para el control de carbohidratos y azúcar. Por favor, proporcione detalles precisos para ayudar a la persona con diabetes a gestionar su condición de manera efectiva.'
        #prompt = 'dime hola'

        st.write("Información de entrada:")
        #st.text_area("Datos Cargados", value=prompt, height=300)

        if st.button("Generar Plan Nutricional"):
            st.session_state.messages = []  # Reiniciar mensajes
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.spinner("Generando plan nutricional..."):
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
                st.session_state.messages.append({"role": "asistente", "content": full_response})

            st.write("Plan Nutricional Generado:")
            st.text_area("Plan Nutricional", value=full_response, height=300)
 
          

if opciones == "Ayuda":
    st.title("CHATBOT - AYUDA")
     
    if "messages" not in st.session_state:
     st.session_state.messages = []

    for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
    # if not st.session_state.get("assistant_introduced"):
    #     # Mensaje inicial para que el asistente asuma el rol de nutricionista
    #     presentacion_asistente = "¡Hola! Soy NutriGod, un nutricionista especializado en diabetes. Estoy aquí para responder todas tus preguntas sobre nutrición y diabetes. Si necesitas información relevante, no dudes en preguntarme y si me falta informacion voy a hacerte algunas preguntitas:). ¿En qué puedo ayudarte hoy?"
    #     st.session_state.messages.append({"role": "assistant", "content": presentacion_asistente})
    #     st.session_state["assistant_introduced"] = True

    if prompt := st.chat_input("escribe tu duda"):
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