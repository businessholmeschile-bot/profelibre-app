import streamlit as st

def render_dashboard():
    # User Hero Section - Clear & Modern
    st.markdown("""
        <div style="margin-bottom: 2.5rem;">
            <h1 style="font-size: 2.8rem; margin-bottom: 0.5rem; color: #111827 !important;">Recupera tus tardes. <br><span style="color: #1D4ED8;">La IA corrige contigo.</span></h1>
            <p style="font-size: 1.25rem; color: #4B5563;">Automatiza la creación de rúbricas, guías y la corrección de pruebas estandarizadas en segundos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # KPI Grid - Light & Shadow (Stitch Style)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                <p style="color: #6B7280; font-size: 0.875rem; font-weight: 600; text-transform: uppercase;">Alumnos PIE</p>
                <p style="color: #111827; font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">12</p>
                <p style="color: #059669; font-size: 0.875rem; font-weight: 500;">↑ 2 este mes</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                <p style="color: #6B7280; font-size: 0.875rem; font-weight: 600; text-transform: uppercase;">Pruebas Creadas</p>
                <p style="color: #111827; font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">45</p>
                <p style="color: #059669; font-size: 0.875rem; font-weight: 500;">↑ 8 hoy</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                <p style="color: #6B7280; font-size: 0.875rem; font-weight: 600; text-transform: uppercase;">Tiempo Recuperado</p>
                <p style="color: #111827; font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">34h</p>
                <p style="color: #059669; font-size: 0.875rem; font-weight: 500;">↑ 4h esta semana</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Feature Cards - Solid Action Cards
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div style="background: white; padding: 2.5rem; border-radius: 12px; border: 1px solid #E5E7EB; height: 320px;">
                <h2 style="color: #1D4ED8 !important;">Generar Evaluación</h2>
                <p style="color: #4B5563; font-size: 1.1rem; margin: 1.5rem 0;">Crea pruebas, guías y rúbricas alineadas al currículum nacional en menos de 2 minutos.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("COMENZAR EVALUACIÓN", use_container_width=True, type="primary", key="btn_gen"):
            st.session_state['page'] = 'Generador'
            st.rerun()

    with c2:
        st.markdown("""
            <div style="background: white; padding: 2.5rem; border-radius: 12px; border: 1px solid #E5E7EB; height: 320px;">
                <h2 style="color: #059669 !important;">Corregir con IA</h2>
                <p style="color: #4B5563; font-size: 1.1rem; margin: 1.5rem 0;">Sube fotos o PDFs de tus pruebas. Nuestra IA detecta respuestas y calcula notas automáticamente.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("INICIAR CORRECCIÓN", use_container_width=True, key="btn_corr"):
            st.info("Función de corrección en desarrollo para la V14.")

    # Recent Activity Section
    st.markdown("<br><h3 style='margin-bottom: 1.5rem;'>Actividad Reciente</h3>", unsafe_allow_html=True)
    
    recent_data = [
        {"Documento": "Evaluación Atencional", "Alumno": "Felipe Soto", "Prioridad": "Alta", "Estado": "Completado ✅"},
        {"Documento": "Guía Comprensión Lector", "Alumno": "Camila Rivas", "Prioridad": "Media", "Estado": "Completado ✅"},
        {"Documento": "Adecuación Visual 1-A", "Alumno": "Amalia Paz", "Prioridad": "Alta", "Estado": "En Revisión ⏳"}
    ]
    st.table(recent_data)
