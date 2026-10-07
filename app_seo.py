import streamlit as st
import google.generativeai as genai

# 1. Configuración básica de la página web
st.set_page_config(page_title="Auditor SEO Baozi", page_icon="🥟", layout="centered")

# 2. Interfaz visual (Títulos y textos)
st.title("🥟 Auditor SEO - Chifa Baozi")
st.write("Herramienta interna para generar estrategias de posicionamiento local en Wanchaq.")

# 3. Panel lateral de seguridad
st.sidebar.header("Configuración")
api_key = st.sidebar.text_input("Ingresa tu API Key de Google", type="password")

# 4. Caja de entrada para el usuario
plato_objetivo = st.text_input("¿Qué plato de la carta deseas auditar?", placeholder="Ej. Sopa Taypá")

# 5. El botón de acción
if st.button("Generar Auditoría"):
    # Reglas de validación
    if not api_key:
        st.warning("⚠️ Por favor, ingresa tu API Key en el panel lateral.")
    elif not plato_objetivo:
        st.warning("⚠️ Por favor, escribe un plato para auditar.")
    else:
        # 6. Conexión y procesamiento
        try:
            with st.spinner('Analizando variables e intención de búsqueda...'):
                genai.configure(api_key=api_key)
                modelo = genai.GenerativeModel('gemini-1.5-flash')
                
                instrucciones = """
                Eres el Auditor SEO Local para Chifa Baozi en Wanchaq, Cusco.
                Tu objetivo es clasificar la intención de búsqueda, proponer keywords 
                hiperlocales y generar un registro CSV al final.
                Restricción absoluta: No inventes volúmenes de búsqueda.
                """
                mensaje = f"Fecha: hoy. Modo: estrategia. Plato: {plato_objetivo}. Entrégame el análisis y el CSV."
                
                solicitud_completa = instrucciones + "\n\n" + mensaje
                respuesta = modelo.generate_content(solicitud_completa)
                
                # 7. Mostrar resultados en la web
                st.success("¡Análisis completado!")
                st.markdown(respuesta.text)
                
        except Exception as error:
            st.error(f"Hubo un error de conexión: {error}")