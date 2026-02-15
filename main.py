import streamlit as st
from components.auth import handle_auth
from components.sidebar import render_sidebar
from views.dashboard import render_dashboard
from views.generator import render_generator
from views.students import render_students

# Page Configuration
st.set_page_config(
    page_title="ProfeLibre - SaaS Educativo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'Dashboard'

def main():
    # Authentication check
    if not st.session_state['user']:
        handle_auth()
    else:
        # Sidebar Navigation
        render_sidebar()
        
        # Routing logic
        if st.session_state['page'] == 'Dashboard':
            render_dashboard()
        elif st.session_state['page'] == 'Generador':
            render_generator()
        elif st.session_state['page'] == 'Estudiantes':
            render_students()

if __name__ == "__main__":
    main()
