import streamlit as st

def render_dashboard():
    st.title("Panel de Control")
    st.write(f"Bienvenido, {st.session_state['user']['email']}")
    
    # KPIs Grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Alumnos PIE", "12", "+2 este mes")
    with col2:
        st.metric("Pruebas Creadas", "45", "+8 hoy")
    with col3:
        st.metric("Tiempo Ahorrado", "34h", "+4h esta semana")
    
    st.markdown("---")
    
    # Action Button
    st.markdown("""
        <div style="text-align: center; padding: 3rem;">
            <h1>🚀 Recupera tu tiempo docente</h1>
            <p>Genera adecuaciones curriculares profesionales en minutos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 COMENZAR NUEVA ADECUACIÓN", use_container_width=True, type="primary"):
        st.session_state['page'] = 'Generador'
        st.rerun()

    # Recent Activity (Placeholder)
    st.subheader("Actividad Reciente")
    st.table({
        "Alumno": ["Felipe Soto", "Camila Rivas", "Amalia Paz"],
        "Fecha": ["15/02/2026", "14/02/2026", "14/02/2026"],
        "Tipo": ["Visual", "Foco", "Comprensión"],
        "Estado": ["Listo ✅", "Listo ✅", "Listo ✅"]
    })
