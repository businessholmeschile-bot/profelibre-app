import streamlit as st

def render_dashboard():
    # User Hero Section
    st.markdown(f"""
        <div style="background: linear-gradient(90deg, #4F46E5, #7C3AED); padding: 2rem; border-radius: 15px; margin-bottom: 2rem; color: white;">
            <h1 style="margin:0; font-size: 2.2rem;">¡Hola, {st.session_state['user']['email'].split('@')[0]}! 👋</h1>
            <p style="font-size: 1.1rem; opacity: 0.9;">Tu asistente pedagógico está listo para una nueva jornada.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # KPIs Grid with Custom CSS
    st.markdown("""
        <style>
        .kpi-card {
            background: rgba(30, 41, 59, 0.7);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: left;
        }
        .kpi-title { color: #94A3B8; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
        .kpi-value { color: white; font-size: 1.8rem; font-weight: 700; margin: 0.5rem 0; }
        .kpi-delta { font-size: 0.85rem; font-weight: 600; }
        .pos { color: #10B981; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="kpi-card">
                <div class="kpi-title">Alumnos PIE</div>
                <div class="kpi-value">12</div>
                <div class="kpi-delta pos">↑ 2 este mes</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="kpi-card">
                <div class="kpi-title">Pruebas Creadas</div>
                <div class="kpi-value">45</div>
                <div class="kpi-delta pos">↑ 8 hoy</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="kpi-card">
                <div class="kpi-title">Tiempo Ahorrado</div>
                <div class="kpi-value">34h</div>
                <div class="kpi-delta pos">↑ 4h esta semana</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Action Card
    st.markdown("""
        <div style="background: rgba(79, 70, 229, 0.1); border: 1px dashed #4F46E5; padding: 2.5rem; border-radius: 15px; text-align: center;">
            <h2 style="color: #818CF8 !important;">🚀 Generador Inteligente</h2>
            <p style="color: #94A3B8; margin-bottom: 2rem;">Sube tu prueba base y genera todas las adecuaciones curriculares en un clic.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("COMENZAR NUEVA ADECUACIÓN", use_container_width=True, type="primary"):
        st.session_state['page'] = 'Generador'
        st.rerun()

    # Recent Activity
    st.markdown("<br>### Actividad Reciente", unsafe_allow_html=True)
    
    recent_data = [
        {"Escenario": "Adecuación Visual", "Alumno": "Felipe Soto", "Prioridad": "Alta", "Estado": "Completado ✅"},
        {"Escenario": "Adecuación Foco", "Alumno": "Camila Rivas", "Prioridad": "Media", "Estado": "Completado ✅"},
        {"Escenario": "Comprensión", "Alumno": "Amalia Paz", "Prioridad": "Alta", "Estado": "En Revisión ⏳"}
    ]
    
    st.table(recent_data)
