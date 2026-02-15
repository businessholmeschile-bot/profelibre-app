import streamlit as st

def render_sidebar():
    with st.sidebar:
        # Logo placeholder
        st.markdown("""
            <div style="text-align: center; padding: 1.5rem 0;">
                <h1 style="color: white !important; font-size: 1.8rem; margin:0;">ProfeLibre 🚀</h1>
                <p style="color: #94A3B8; font-size: 0.8rem;">Arquitectura Educativa AI</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Navigation with custom styling (buttons are already styled in main.py)
        if st.button("🏠 DASHBOARD", use_container_width=True):
            st.session_state['page'] = 'Dashboard'
            st.rerun()
            
        if st.button("🚀 GENERADOR", use_container_width=True):
            st.session_state['page'] = 'Generador'
            st.rerun()
            
        if st.button("👥 ALUMNOS PIE", use_container_width=True):
            st.session_state['page'] = 'Estudiantes'
            st.rerun()
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Profe AI Consultor Card
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.03); padding: 1rem; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
                <p style="color: #818CF8; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;">🤖 Consultor IA</p>
                <p style="color: #94A3B8; font-size: 0.8rem;">¿Cómo puedo ayudarte hoy con alguna adecuación?</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # User Info & Logout
        st.markdown("---")
        st.caption(f"Sesión: {st.session_state['user']['email']}")
        if st.button("Cerrar Sesión", use_container_width=True):
            st.session_state['user'] = None
            st.rerun()
