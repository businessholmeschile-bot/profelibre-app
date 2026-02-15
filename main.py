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

# Global CSS for Stitch Identity (FORCE Light Theme)
def local_css():
    st.markdown("""
        /* Force Light Theme Overrides - High Specificity */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main, .stApp {
            background-color: #F9FAFB !important;
            background-image: none !important;
            color: #111827 !important;
        }

        :root {
            --primary-color: #1D4ED8;
            --bg-color: #F9FAFB;
            --sidebar-bg: #FFFFFF;
            --card-bg: #FFFFFF;
            --text-main: #111827;
            --text-muted: #6B7280;
        }

        .main {
            background-color: #F9FAFB !important;
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Outfit', sans-serif !important;
            color: #111827 !important;
        }

        p, span, div, label {
            font-family: 'Inter', sans-serif !important;
            color: #374151 !important;
        }

        /* Clean Cards with Subtle Shadows */
        .stMetric, .stTable, div[data-testid="stExpander"], div[data-testid="stVerticalBlock"] > div[style*="background"] {
            background: #FFFFFF !important;
            border-radius: 8px !important;
            padding: 1.5rem !important;
            border: 1px solid #E5E7EB !important;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06) !important;
        }

        /* Buttons Styling - Solid Blue */
        .stButton>button {
            border-radius: 6px !important;
            background-color: #1D4ED8 !important;
            color: white !important;
            border: none !important;
            padding: 0.5rem 1.5rem !important;
            font-weight: 600 !important;
        }
        
        .stButton>button:hover {
            background-color: #1E40AF !important;
        }

        /* Sidebar Styling - Force White */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E5E7EB !important;
        }
        
        section[data-testid="stSidebar"] * {
            color: #374151 !important;
        }

        /* Input Styling - Force Light */
        .stTextInput>div>div>input {
            border-radius: 6px !important;
            border: 1px solid #D1D5DB !important;
            background-color: white !important;
            color: #111827 !important;
        }
        
        /* Hide Streamlit Header/Footer for Premium Look */
        header, footer { visibility: hidden !important; }
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
