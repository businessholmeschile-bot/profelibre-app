import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("ProfeLibre")
        st.caption("Arquitecto: ProfeLibre AI")
        st.markdown("---")
        
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state['page'] = 'Dashboard'
            st.rerun()
            
        if st.button("🚀 Nueva Adecuación", use_container_width=True):
            st.session_state['page'] = 'Generador'
            st.rerun()
            
        if st.button("👥 Alumnos PIE", use_container_width=True):
            st.session_state['page'] = 'Estudiantes'
            st.rerun()
            
        st.markdown("---")
        
        # Profe AI Consultor
        st.subheader("🤖 Profe AI Consultor")
        with st.expander("¿Necesitas ayuda?", expanded=False):
            st.write("Hola, soy tu consultor pedagógico.")
            user_msg = st.text_input("Escribe tu duda...")
            if user_msg:
                st.info("Simulación: Estoy procesando tu consulta pedagógica...")
                st.success("Sugerencia: Intenta usar el perfil 'Foco' para alumnos con TDAH.")

        st.markdown("---")
        if st.button("Cerrar Sesión"):
            st.session_state['user'] = None
            st.rerun()
