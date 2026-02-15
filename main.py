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

# Global CSS for Stitch Identity (Light Theme)
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700&display=swap');
        
        :root {
            --primary-color: #1D4ED8; /* Azul Stitch */
            --bg-color: #F9FAFB;
            --sidebar-bg: #FFFFFF;
            --card-bg: #FFFFFF;
            --text-main: #111827;
            --text-muted: #6B7280;
        }

        .main {
            background-color: var(--bg-color);
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Outfit', sans-serif !important;
            color: var(--text-main) !important;
        }

        p, span, div {
            font-family: 'Inter', sans-serif;
        }

        /* Clean Cards with Subtle Shadows */
        .stMetric, .stTable, div[data-testid="stExpander"] {
            background: var(--card-bg);
            border-radius: 8px;
            padding: 1.5rem;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        }

        /* Buttons Styling - Solid Blue */
        .stButton>button {
            border-radius: 6px;
            background-color: var(--primary-color) !important;
            color: white !important;
            border: none;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: background 0.2s;
        }
        
        .stButton>button:hover {
            background-color: #1E40AF !important;
            border: none;
        }

        /* Sidebar Styling - White and Clean */
        section[data-testid="stSidebar"] {
            background-color: var(--sidebar-bg) !important;
            border-right: 1px solid #E5E7EB;
        }
        
        [data-testid="stSidebarNav"] {
            background-color: var(--sidebar-bg) !important;
        }

        /* Input Styling */
        .stTextInput>div>div>input {
            border-radius: 6px;
            border: 1px solid #D1D5DB;
        }
        </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'Dashboard'

def main():
    local_css()
    
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
