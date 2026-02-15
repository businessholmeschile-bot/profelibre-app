import streamlit as st

def render_sidebar():
    with st.sidebar:
        # Logo Context from Stitch
        st.markdown("""
            <div style="text-align: center; padding: 1rem 0 2rem 0; border-bottom: 1px solid #F3F4F6; margin-bottom: 1.5rem;">
                <h2 style="color: #111827 !important; margin: 0; font-size: 1.5rem;">ProfeLibre 🚀</h2>
                <p style="color: #9CA3AF; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 5px;">EduIA Chile</p>
            </div>
        """, unsafe_allow_html=True)

        # Menu Items exactly like Stitch sidebar
        menu_items = [
            {"label": "Dashboard", "id": "Dashboard", "icon": "🏠"},
            {"label": "Generador", "id": "Generador", "icon": "📝"},
            {"label": "Corrección IA", "id": "Corrección", "icon": "🤖"},
            {"label": "Banco Personal", "id": "Banco", "icon": "📂"},
            {"label": "Estadísticas", "id": "Estadisticas", "icon": "📊"}
        ]

        for item in menu_items:
            active = st.session_state['page'] == item['id']
            style = "background: #EFF6FF; color: #1D4ED8; font-weight: 700; border-radius: 8px;" if active else "color: #4B5563;"
            
            if st.button(f"{item['icon']}  {item['label']}", key=f"nav_{item['id']}", use_container_width=True):
                st.session_state['page'] = item['id']
                st.rerun()

        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Secondary Menu
        st.markdown("---")
        if st.button("⚙️ Configuración", use_container_width=True):
            st.info("Próximamente")
            
        # User Profile Mini-Card at Bottom
        st.markdown("""
            <div style="position: fixed; bottom: 20px; left: 20px; width: 220px; background: white; padding: 12px; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 10px;">
                <div style="width: 32px; height: 32px; background: #E5E7EB; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; color: #6B7280;">D</div>
                <div>
                    <p style="margin: 0; font-size: 0.85rem; font-weight: 700; color: #111827;">Docente Pro</p>
                    <p style="margin: 0; font-size: 0.7rem; color: #9CA3AF;">Liceo Polivalente</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Cerrar Sesión", use_container_width=True, type="secondary"):
            st.session_state['user'] = None
            st.session_state['page'] = 'Home'
            st.session_state['show_login'] = False
            st.rerun()
