import openai
import streamlit as st
from PIL import Image


#configuracion de navegacion
st.set_page_config(
    page_title="NutriGod",
    page_icon="https://i.pinimg.com/564x/ba/94/c7/ba94c795f764689da26822a6da41d9ce.jpg",
    layout="wide",  # Opcional: Puedes personalizar el diseño
    #initial_sidebar_state="expanded",  # Opcional: Expande la barra lateral por defecto
)

# Configuración de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Función para respuestas gpt
def interactuar_con_modelo(prompt):
    st.session_state.messages = []  # Reiniciar mensajes
    st.session_state.messages.append({"role": "user", "content": prompt})

    #with st.spinner("Generando respuesta..."):
    with st.spinner("Generando respuesta..."):
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
     return full_response

st.sidebar.title("Barra de opciones")
opciones = st.sidebar.radio("Seleccione una actividad", ["inicio", "Carga de Datos", "Plan Nutricional", "Ayuda"])

#inicio--------------------------------------------------------------------

if opciones == "inicio":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(
            f'<div style="display: flex; justify-content: center; align-items: center; height: 250px;">'
            f'<img src="https://i.pinimg.com/564x/ba/94/c7/ba94c795f764689da26822a6da41d9ce.jpg" style="width:200px; height:200px;">'
            f'</div>',
            unsafe_allow_html=True
            )
            
    with col2:
        st.title("Nutrigod")
        st.header("Bienvenido a Nutrigod")
        st.markdown(
                "<div style='background-color:#0B173B; padding: 20px; border-radius: 10px;'>"
                """<p style='font-size: 16px; text-align: justify;'>
                En Nutrigod, nuestra misión es simple pero poderosa: <strong>mejorar la calidad de vida de las personas con diabetes</strong> a través de la tecnología y la inteligencia artificial.<br>
                ¿Cómo lo logramos? A través de <strong>Nutrigod</strong>, una innovadora aplicación diseñada para brindarte un <strong>control efectivo de tu salud</strong>.
                <br>
                </p>"""
                "</div>",
                unsafe_allow_html=True
            ) 
    st.write("")  
    col1, col2 = st.columns([2, 1])
    with col2:
        st.write(
            f'<div style="display: flex; justify-content: center; align-items: center; height: 340px;">'
            f'<img src="https://i.pinimg.com/originals/79/f9/7e/79f97e91f965b8a000d09244c1d9332e.gif" style="width:250px; height:250px;">'
            f'</div>',
            unsafe_allow_html=True
            )
            
    with col1:
     st.markdown(
                 "<div style='background-color:#0B173B ; padding: 20px; border-radius: 10px;'>"
                """  
                <p><strong>¿Que funciones tiene Nutrigod?:</strong></p>
                <ul>
                  <li>Genera recomendaciones de alimentación personalizadas con inteligencia artificial.</li>
                  <li>Controla constantemente tus niveles de glucosa.</li>
                  <li>Asesoramiento en cualquier momento atravez de un chatbot.</li>
                </ul>
                <p><strong>Beneficios para Ti:</strong></p>
                <ul>
                 <li>Mejor Gestión de tu Salud: Decisiones informadas sobre tu bienestar.</li>
                 <li>Dieta Personalizada: Alimentación adaptada a tus necesidades y preferencias.</li>
                 <li>Mayor Conocimiento sobre tu Diabetes: Educación y empoderamiento.</li>
                </ul>
                """
                "</div>",
                unsafe_allow_html=True
            )
    col3, col4 = st.columns([2, 3])
    with col3:
               st.write(
            f'<div style="display: flex; justify-content: center; align-items: center; height: 400px;">'
            f'<img src="https://turkiye.ai/wp-content/uploads/2021/05/saglikta-yapay-zeka.jpg" style="width:450px; height:250px;">'
            f'</div>',
            unsafe_allow_html=True
            )
    with col4:
        st.write("")
        st.markdown(
                "<div style='background-color:#0B173B ; padding: 20px; border-radius: 10px;'>"
                """
                <p><strong>Facilidad de Uso:</strong></p>
                <p>Nutrigod está diseñado pensando en ti, sea cual sea tu nivel de familiaridad con la tecnología. Es intuitivo, amigable y fácil de usar. No importa si eres un experto en tecnología o si recién estás comenzando, Nutrigod te acompañará en tu viaje..</p>
                <p><strong>Nuestro Compromiso con tu Salud:</strong></p>
                <p>En Nutrigod, estamos dedicados a tu bienestar. Nuestra aplicación se basa en la innovación y la mejora constante. Trabajamos incansablemente para proporcionarte las mejores herramientas y recursos para el manejo de la diabetes.</p>
                <p><strong>¿Estás listo para tomar el control de tu salud y vivir una vida más saludable con diabetes?</strong></p>
                <p>¡Únete a Nutrigod hoy mismo! Puedes descargar la aplicación, registrarte o explorar más sobre cómo Nutrigod puede marcar la diferencia en tu vida.</p>
             """
             "</div>",
                unsafe_allow_html=True
            ) 

#datos-----------------------------------------------------------------------

if opciones == "Carga de Datos":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(
            f'<div style="display: flex; justify-content: center; align-items: center; height: 250px;">'
            f'<img src="https://i.pinimg.com/564x/ba/94/c7/ba94c795f764689da26822a6da41d9ce.jpg" style="width:200px; height:200px;">'
            f'</div>',
            unsafe_allow_html=True
            )
    with col2:
        st.title("Nutrigod")
        st.header("CARGA DE DATOS")
        st.write("Por favor complete todos los campos con sus datos para poder generar su plan nutricional:")
        # Inicializar o cargar datos del usuario
    user_data = st.session_state.get("user_data", {
        "nombre": "",
        "glucosa en ayunas": "",
        "glucosa despues de comidas": "",
        "preferencias alimenticias": "",
        "renstricciones": "",
        "Objetivos de salud": "",
        "Tipo de diabetes": "",
        "Informacion medica": "",
        "Edad": "",
        "Genero": "",
        "Peso": "",
        "Estatura": "",
        "Actividad fisica": "",
        "Medicamentos": ""
    })

    # Formulario para ingresar datos
    with st.form(key='user_data_form'):
     user_nombre = st.text_input("¿cual es su nombre?", user_data["nombre"])
     user_glucosaAyuna = st.text_input("¿cual es nivel de glucosa en ayunas?", user_data["glucosa en ayunas"])
     user_glucosaDespuesDeComer = st.text_input("¿cual es nivel de glucosa despues de comer?", user_data["glucosa despues de comidas"])
     user_preferencias = st.text_input("¿Que comidas les gusta y cuales no les gusta?", user_data["preferencias alimenticias"])
     user_renstricciones = st.text_input("¿tiene alguna renstriccion dietetica o alergias?", user_data["renstricciones"])
     user_objetivos = st.text_input("¿Estás buscando perder , mantenerlo o ganar peso?", user_data["Objetivos de salud"])
     user_tipoDeDiabetes = st.text_input("¿Qué tipo de diabetes tiene?", user_data["Tipo de diabetes"])
     user_infoMedica = st.text_input("¿Hay alguna otra condición médica relevante además de la diabetes?", user_data["Informacion medica"])
     user_edad = st.text_input("¿Qué edad tiene?", user_data["Edad"])
     user_genero = st.text_input("¿Qué género es?", user_data["Genero"])
     user_peso = st.text_input("Peso (kg):", user_data["Peso"])
     user_estatura = st.text_input("Altura (cm):", user_data["Estatura"])
     user_actividad = st.text_input("¿Cuánto ejercicio realiza regularmente?", user_data["Actividad fisica"])
     user_medicamentos = st.text_input("¿Está tomando medicamento para controlar la diabetes?", user_data["Medicamentos"])

     if st.form_submit_button("Guardar Datos"):
        campos_obligatorios = [user_objetivos,user_actividad,user_edad,user_estatura,user_genero,user_glucosaAyuna,user_glucosaDespuesDeComer,user_infoMedica,user_medicamentos,user_nombre,user_peso,user_preferencias,user_renstricciones,user_tipoDeDiabetes]
        if all(campos_obligatorios):
        # Guardar datos en session_state
            user_data = {
             "nombre": user_nombre,
             "glucosa en ayunas": user_glucosaAyuna,
             "glucosa despues de comidas": user_glucosaDespuesDeComer,
             "preferencias alimenticias": user_preferencias,
             "renstricciones": user_renstricciones,
             "Objetivos de salud": user_objetivos,
             "Tipo de diabetes": user_tipoDeDiabetes,
             "Informacion medica": user_infoMedica,
             "Edad": user_edad,
             "Genero": user_genero,
             "Peso": user_peso,
             "Estatura": user_estatura,
             "Actividad fisica": user_actividad,
             "Medicamentos": user_medicamentos,
             }
            st.session_state.user_data = user_data
            st.success("Datos guardados correctamente.")
        else:
         st.warning("Por favor, complete todos los campos obligatorios.")
    
#plan nutricional---------------------------------------

if opciones == "Plan Nutricional":
    st.title("NutriGod - Plan Nutricional")
    st.image("https://i.pinimg.com/564x/ba/94/c7/ba94c795f764689da26822a6da41d9ce.jpg", use_column_width=False, width=200)
    if "user_data" not in st.session_state:
        st.warning("Por favor, cargue los datos en la opción 'Carga de Datos' primero.")
    else:
        user_data = st.session_state.user_data
        prompt = f"Quiero que actúes como un profesional nutricional especializado en diabetes y interpretes los datos proporcionados. Genera un plan nutricional personalizado en forma de tabla 5x7 para cada día de la semana teniendo en cuenta los siguientes datos:\nNombre: {user_data['nombre']}. Nivel de glucosa en ayunas: {user_data['glucosa en ayunas']}. Nivel de glucosa después de las comidas: {user_data['glucosa despues de comidas']}. Preferencias alimenticias: {user_data['preferencias alimenticias']}. Restricciones dietéticas o alergias: {user_data['renstricciones']}. Objetivo de peso: {user_data['Objetivos de salud']}. Tipo de diabetes: {user_data['Tipo de diabetes']}. Información médica relevante: {user_data['Informacion medica']}. Edad y género: {user_data['Edad']}, {user_data['Genero']}. Peso corporal: {user_data['Peso']}. Estatura: {user_data['Estatura']}. Nivel de actividad física: {user_data['Actividad fisica']}. Medicamentos actuales: {user_data['Medicamentos']}."                  
    if st.button("Generar Plan Nutricional"):
         with st.chat_message("assistant"):
            respuesta = interactuar_con_modelo(prompt)
            message_placeholder = st.empty()
            message_placeholder.markdown(respuesta + "▌")
         st.session_state.messages.append({"role": "assistant", "content": respuesta})

#ayuda-----------------------------------------------------------

if opciones == "Ayuda":
    st.title("CHATBOT - AYUDA")
    st.header("Hola!")
    st.write("¡Bienvenido a nuestra sección de ayuda! Estamos aquí para responder a tus preguntas y brindarte la asistencia que necesitas. ¿Tienes alguna duda o necesitas orientación? ¡No dudes en preguntar! Estamos aquí para ayudarte.")
    url = "https://i.pinimg.com/originals/a4/81/1d/a4811dcfd85b23cdd91ceb1ea9b959d6.gif"
    st.image(url, caption='', use_column_width=False, width=200)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Escribe tu duda"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            respuesta = interactuar_con_modelo(prompt)
            message_placeholder = st.empty()
            message_placeholder.markdown(respuesta + "▌")
        st.session_state.messages.append({"role": "assistant", "content": respuesta})