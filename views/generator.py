import streamlit as st
import pandas as pd
from logic.engine_v13 import CoreEngineV13
import io

def render_generator():
    st.title("🚀 Generador de Adecuaciones")
    
    if 'wizard_step' not in st.session_state:
        st.session_state['wizard_step'] = 1
    
    # Progress Bar
    steps = ["Carga", "Selección", "Ajustes", "Resultados"]
    st.progress(st.session_state['wizard_step'] / 4)
    cols_steps = st.columns(4)
    for i, step in enumerate(steps):
        if st.session_state['wizard_step'] == i+1:
            cols_steps[i].markdown(f"**{i+1}. {step}**")
        else:
            cols_steps[i].markdown(f"{i+1}. {step}")

    st.markdown("---")

    if st.session_state['wizard_step'] == 1:
        render_step_1()
    elif st.session_state['wizard_step'] == 2:
        render_step_2()
    elif st.session_state['wizard_step'] == 3:
        render_step_3()
    elif st.session_state['wizard_step'] == 4:
        render_step_4()

    # Navigation Buttons
    st.markdown("---")
    col_nav1, col_nav2 = st.columns([1, 1])
    with col_nav1:
        if st.session_state['wizard_step'] > 1:
            if st.button("⬅️ Anterior"):
                st.session_state['wizard_step'] -= 1
                st.rerun()
    with col_nav2:
        if st.session_state['wizard_step'] < 4:
            if st.button("Siguiente ➡️"):
                st.session_state['wizard_step'] += 1
                st.rerun()

def render_step_1():
    st.header("Paso 1: Carga de Archivos e Integraciones")
    st.info("Sube documentos (Word, PDF), fotos de ejercicios o vincula Google Docs.")
    
    # Selection of input type
    input_type = st.radio("Método de entrada de la Prueba:", ["Archivo (Word/PDF/Imagen)", "URL Google Docs"], horizontal=True)
    
    if input_type == "Archivo (Word/PDF/Imagen)":
        st.session_state['source_file'] = st.file_uploader("Prueba Estándar", type=['docx', 'pdf', 'png', 'jpg', 'jpeg'])
    else:
        st.session_state['google_url'] = st.text_input("Pega la URL del Google Doc", placeholder="https://docs.google.com/document/d/...")
    
    st.markdown("---")
    st.session_state['matrix_file'] = st.file_uploader("Matriz de Respuestas (.xlsx)", type=['xlsx'])
    st.session_state['roster_file'] = st.file_uploader("Nómina de Alumnos (.xlsx)", type=['xlsx'])
    st.session_state['logo_file'] = st.file_uploader("Logo Institucional (.png)", type=['png'])

def render_step_2():
    st.header("Paso 2: Selección de Alumnos")
    if 'roster_file' in st.session_state and st.session_state['roster_file']:
        try:
            df = pd.read_excel(st.session_state['roster_file'])
            st.write("Selecciona los alumnos para los que deseas generar adecuaciones:")
            
            selected_indices = []
            for i, row in df.iterrows():
                col_a, col_b, col_c = st.columns([0.1, 0.5, 0.4])
                is_selected = col_a.checkbox("", key=f"sel_{i}")
                if is_selected:
                    selected_indices.append(i)
                col_b.write(f"**{row['Nombre']}** ({row['Perfil']})")
                # Toggle "No borrar D" added to session state for processing
                no_d = col_c.toggle("No borrar D", key=f"toggle_{i}")
                df.at[i, 'No borrar D'] = no_d
            
            st.session_state['selected_students_df'] = df.iloc[selected_indices]
        except Exception as e:
            st.error(f"Error al leer la nómina: {e}")
    else:
        st.warning("Primero debes subir la nómina en el Paso 1.")

def render_step_3():
    st.header("Paso 3: Previsualización y Ajustes")
    
    # New: OCR / Extraction Preview
    if 'source_file' in st.session_state and st.session_state['source_file']:
        with st.expander("🔍 Previsualizar contenido extraído", expanded=True):
            with st.spinner("Extrayendo texto..."):
                engine = CoreEngineV13(roster_df=pd.DataFrame())
                f_ext = st.session_state['source_file'].name.split('.')[-1].lower()
                content = engine.load_source(st.session_state['source_file'], f_ext)
                st.text_area("Texto detectado:", value=content, height=300)
    
    st.markdown("---")
    st.write("Añade instrucciones adicionales para la personalización por IA.")
    st.text_area("Instrucciones adicionales", placeholder="Ej: Simplificar lenguaje en preguntas de desarrollo...")

def render_step_4():
    st.header("Paso 4: Resultados")
    if st.button("⚙️ GENERAR DOCUMENTOS"):
        with st.spinner("Procesando adecuaciones con Core Engine v13.2..."):
            try:
                engine = CoreEngineV13(
                    roster_df=pd.read_excel(st.session_state['roster_file']),
                    logo_img=st.session_state['logo_file'].getvalue() if st.session_state['logo_file'] else None
                )
                
                # Load source
                if 'source_file' in st.session_state and st.session_state['source_file']:
                    f_ext = st.session_state['source_file'].name.split('.')[-1].lower()
                    engine.load_source(st.session_state['source_file'], f_ext)
                    source_for_gen = st.session_state['source_file'] if f_ext == 'docx' else None
                elif 'google_url' in st.session_state:
                    engine.load_source(st.session_state['google_url'], 'google_url')
                    source_for_gen = None
                
                zip_data = engine.generate_all(
                    st.session_state['selected_students_df'], 
                    pd.read_excel(st.session_state['matrix_file']),
                    source_file=source_for_gen
                )
                
                st.success("¡Adecuaciones generadas con éxito!")
                st.download_button(
                    label="📥 Descargar ZIP de Resultados",
                    data=zip_data,
                    file_name="Adecuaciones_ProfeLibre.zip",
                    mime="application/zip",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error durante el procesamiento: {e}")
