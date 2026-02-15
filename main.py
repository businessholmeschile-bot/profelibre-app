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

# Global CSS for Stitch Identity
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@400;600;700&display=swap');
        
        :root {
            --primary-color: #4F46E5;
            --secondary-color: #818CF8;
            --bg-color: #0F172A;
            --card-bg: rgba(30, 41, 59, 0.7);
            --text-main: #F8FAFC;
        }

        .main {
            background-color: var(--bg-color);
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Outfit', sans-serif !important;
            color: var(--text-main) !important;
        }

        /* Glassmorphism Card Wrapper */
        .stMetric, .stTable {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        /* Customize Buttons */
        .stButton>button {
            border-radius: 8px;
            background-color: var(--primary-color) !important;
            color: white !important;
            border: none;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary-color) !important;
            box-shadow: 0 0 15px var(--primary-color);
            transform: translateY(-2px);
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #1E293B !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .sidebar-content {
            padding: 1.5rem;
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
