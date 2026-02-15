import streamlit as st
import openpyxl
from logic.engine_v13 import CoreEngineV13
import io

def excel_to_list_of_dicts(file):
    if not file:
        return []
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    data = []
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))
    return data

def render_generator():
    # Header from Stitch
    st.markdown("""
        <div style="margin-bottom: 2rem;">
            <h1 style="font-size: 2.2rem; font-weight: 600; color: #111827 !important; margin-bottom: 0.3rem;">Generador de Evaluaciones</h1>
            <p style="color: #6B7280;">Diseña instrumentos de evaluación alineados al currículum nacional en segundos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if 'wizard_step' not in st.session_state:
        st.session_state['wizard_step'] = 1
    
    # Premium Stepper from Stitch (5 Steps)
    steps = ["Identificación", "Currículum", "Configuración", "Formato", "Revisión"]
    
    # Stepper UI
    cols = st.columns(len(steps))
    for i, step in enumerate(steps):
        step_num = i + 1
        active = st.session_state['wizard_step'] == step_num
        color = "#1D4ED8" if active else "#9CA3AF"
        bg = "#EFF6FF" if active else "transparent"
        cols[i].markdown(f"""
            <div style="text-align: center; border-bottom: 3px solid {color}; padding-bottom: 10px; background: {bg}; border-radius: 8px 8px 0 0;">
                <span style="color: {color}; font-weight: {700 if active else 400}; font-size: 0.8rem;">{step_num}. {step}</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Two-Column Layout like Stitch
    col_left, col_right = st.columns([0.6, 0.4])

    with col_left:
        if st.session_state['wizard_step'] == 1:
            st.markdown("### 1. Identificación")
            st.session_state['curso'] = st.selectbox("CURSO", ["1° Básico", "2° Básico", "1° Medio", "2° Medio"], index=2)
            st.session_state['asignatura'] = st.selectbox("ASIGNATURA", ["Matemática", "Lengua y Literatura", "Historia", "Ciencias"], index=1)
            st.markdown("---")
            st.session_state['nivel_dificultad'] = st.select_slider("Nivel de Dificultad", options=["Bajo", "Medio", "Alto"], value="Medio")
            
        elif st.session_state['wizard_step'] == 2:
            st.markdown("### 2. Objetivos de Aprendizaje (OA)")
            oas = [
                {"code": "OA 03", "desc": "Analizar críticamente textos de diversos géneros no literarios."},
                {"code": "OA 08", "desc": "Formular una interpretación de los textos leídos o vistos."},
                {"code": "OA 12", "desc": "Aplicar estrategias de comprensión de lectura acorde a sus objetivos."}
            ]
            for oa in oas:
                st.markdown(f"""
                    <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 0.8rem;">
                        <input type="checkbox" id="{oa['code']}" checked>
                        <label for="{oa['code']}" style="margin-left: 10px; font-weight: 600;">{oa['code']}</label>
                        <p style="margin: 5px 0 0 25px; font-size: 0.85rem; color: #6B7280;">{oa['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)

        elif st.session_state['wizard_step'] == 3:
            st.markdown("### 3. Configuración de Ítems")
            st.session_state['item_types'] = st.multiselect("Tipos de Ítem", ["Opción Múltiple", "Desarrollo", "Verdadero/Falso", "Términos Pareados"], default=["Opción Múltiple", "Desarrollo"])
            st.number_input("Cantidad de preguntas", min_value=1, max_value=50, value=15)
            
        elif st.session_state['wizard_step'] == 4:
            st.markdown("### 4. Formato y Adecuaciones")
            st.session_state['adecuacion'] = st.radio("Tipo de Adecuación (PIE)", ["Ninguna", "Visual", "Lectura Fácil (TEA/TDAH)", "Simplificación"], index=2)
            st.file_uploader("Subir base (opcional)", type=['docx', 'pdf'])

        elif st.session_state['wizard_step'] == 5:
            st.markdown("### 5. Revisión Final")
            st.success("Configuración lista para generar.")
            if st.button("🪄 Generar Evaluación", type="primary", use_container_width=True):
                st.balloons()
                st.success("¡Documento generado con éxito!")

    with col_right:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 4px; border: 1px solid #D1D5DB; min-height: 500px; box-shadow: 10px 10px 0px #F3F4F6; margin-left: 20px;">
                <p style="color: #9CA3AF; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2rem;">Vista Previa AI</p>
                <div style="border-bottom: 2px solid #E5E7EB; padding-bottom: 10px; margin-bottom: 2rem;">
                    <h4 style="margin: 0;">Evaluación de Lenguaje</h4>
                    <p style="font-size: 0.8rem; color: #6B7280; margin: 5px 0;">2° Medio - Unidad 1</p>
                </div>
                <div style="color: #4B5563; font-family: serif; line-height: 1.6;">
                    <p style="font-weight: bold;">I. Comprensión Lectora</p>
                    <p style="font-size: 0.9rem;">Lea el siguiente fragmento y responda...</p>
                    <div style="margin-top: 15px; width: 100%; height: 8px; background: #F3F4F6; border-radius: 4px;"></div>
                    <div style="margin-top: 8px; width: 80%; height: 8px; background: #F3F4F6; border-radius: 4px;"></div>
                    <div style="margin-top: 8px; width: 90%; height: 8px; background: #F3F4F6; border-radius: 4px;"></div>
                </div>
                <div style="margin-top: 100px; text-align: center; color: #D1D5DB;">
                    <p style="font-size: 0.8rem;">[ El contenido aparecerá aquí ]</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Footer navigation
    st.markdown("<br><br>", unsafe_allow_html=True)
    fcol1, fcol2, fcol3 = st.columns([1, 2, 1])
    with fcol1:
        if st.session_state['wizard_step'] > 1:
            if st.button("Anterior"):
                st.session_state['wizard_step'] -= 1
                st.rerun()
    with fcol3:
        if st.session_state['wizard_step'] < 5:
            if st.button("Siguiente", type="primary"):
                st.session_state['wizard_step'] += 1
                st.rerun()
