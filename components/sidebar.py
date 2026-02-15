import streamlit as st

def render_sidebar():
    with st.sidebar:
        # Logo & App Identity
        st.markdown("""
            <div style="padding: 1.5rem 0; border-bottom: 1px solid #F3F4F6; margin-bottom: 2rem;">
                <h1 style="color: #1D4ED8 !important; font-size: 1.8rem; margin:0; font-weight: 800;">ProfeLibre</h1>
                <p style="color: #6B7280; font-size: 0.85rem; margin-top: 0.25rem;">Panel Docente</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation Menu
        # The buttons are styled globally in main.py, but we can refine them here
        if st.button("📊 Dashboard", use_container_width=True, type="secondary"):
            st.session_state['page'] = 'Dashboard'
            st.rerun()
            
        if st.button("🚀 Generador", use_container_width=True, type="secondary"):
            st.session_state['page'] = 'Generador'
            st.rerun()
            
        if st.button("👥 Alumnos PIE", use_container_width=True, type="secondary"):
            st.session_state['page'] = 'Estudiantes'
            st.rerun()
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Profile & Context (Mocking the user info at bottom)
        st.markdown("""
            <div style="background: #F9FAFB; padding: 1rem; border-radius: 8px; border: 1px solid #E5E7EB; margin-top: 5rem;">
                <p style="color: #374151; font-weight: 600; font-size: 0.9rem; margin: 0;">Profe Maria</p>
                <p style="color: #6B7280; font-size: 0.75rem; margin: 0;">Liceo Bicentenario</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Logout
        if st.button("Cerrar Sesión", use_container_width=True):
            st.session_state['user'] = None
            st.rerun()
