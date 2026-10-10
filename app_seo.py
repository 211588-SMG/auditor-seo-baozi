import streamlit as st
import google.generativeai as genai

# 1. Configuración de página con título e ícono
st.set_page_config(
    page_title="Auditor SEO Baozi", 
    page_icon="🥟", 
    layout="centered"
)

# 2. Inyección de diseño profesional (Estilos CSS personalizados)
st.markdown("""
    <style>
    /* Estilo para el fondo y contenedor principal */
    .stApp {
        background-color: #11141c;
        color: #e2e8f0;
    }
    
    /* Personalización del título con degradado */
    .title-banner {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    /* Subtítulo */
    .subtitle-text {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Tarjetas de resultados */
    .card-dashboard {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Botón de acción mejorado */
    .stButton>button {
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 0.6rem 2rem !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(217, 119, 6, 0.3) !important;
    }
    
    /* Estilos para badges (etiquetas) */
    .badge {
        display: inline-block;
        background-color: #334155;
        color: #f59e0b;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Interfaz visual (Título y Banner)
st.markdown('<div class="title-banner">🥟 Auditor SEO - Chifa Baozi</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Plataforma de Inteligencia Artificial para el posicionamiento local de Chifa Baozi en Wanchaq, Cusco.</div>', unsafe_allow_html=True)

# 4. Panel lateral de configuración
st.sidebar.markdown("### 🛠️ Configuración")
api_key = st.sidebar.text_input("Ingresa tu API Key de Google", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Parámetros del Agente")
creatividad = st.sidebar.slider("Temperatura de creatividad", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
ubicacion = st.sidebar.selectbox("Localización objetivo", ["Wanchaq, Cusco", "Todo Cusco", "San Jerónimo"])

# 5. Entrada principal (Input del plato)
plato_objetivo = st.text_input("¿Qué plato de la carta deseas auditar?", placeholder="Ej. Combinado de pato asado")

# 6. Acción de Generar Auditoría
if st.button("✨ Generar Auditoría"):
    if not api_key:
        st.warning("⚠️ Por favor, ingresa tu API Key en el panel lateral.")
    elif not plato_objetivo:
        st.warning("⚠️ Por favor, escribe un plato para auditar.")
    else:
        try:
            with st.spinner('Analizando variables e intención de búsqueda...'):
                genai.configure(api_key=api_key)
                # Forzar el modelo pro garantizado en tu servidor
                modelo = genai.GenerativeModel('gemini-2.5-flash-lite')
                
                # Reglas estrictas en formato HTML o formato legible
                instrucciones = f"""
                Eres el Auditor SEO Local para Chifa Baozi en {ubicacion}.
                Tu objetivo es clasificar la intención de búsqueda, proponer keywords 
                hiperlocales y generar un registro CSV al final.
                No inventes volúmenes de búsqueda.
                """
                
                mensaje = f"Modo: estrategia. Plato: {plato_objetivo}. Entrégame el análisis detallado y el CSV final."
                
                solicitud_completa = instrucciones + "\n\n" + mensaje
                respuesta = modelo.generate_content(solicitud_completa)
                
                # Mostrar el resultado final con un formato moderno de tarjetas
                st.success("¡Análisis completado con éxito!")
                
                # Renderizar los resultados de la IA en la página con estilo Markdown estándar
                st.markdown(respuesta.text)
                
        except Exception as error:
            st.error(f"Hubo un error de conexión: {error}")
