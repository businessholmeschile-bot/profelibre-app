from supabase import create_client, Client
import streamlit as st

def get_supabase_client() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

def handle_auth():
    st.markdown("""
        <style>
        .auth-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 4rem 1rem;
            background-color: #F9FAFB !important;
            min-height: 80vh;
        }
        .auth-card {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 3rem;
            width: 100%;
            max-width: 420px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            text-align: center;
        }
        .auth-title {
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            color: #111827;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .auth-subtitle {
            font-family: 'Inter', sans-serif;
            color: #6B7280;
            margin-bottom: 2.5rem;
            font-size: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="auth-title">ProfeLibre 🚀</h1>', unsafe_allow_html=True)
    st.markdown('<p class="auth-subtitle">SaaS Educativo para Docentes Modernos</p>', unsafe_allow_html=True)
    
    email = st.text_input("Correo electrónico", placeholder="ejemplo@correo.cl")
    password = st.text_input("Contraseña", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Iniciar Sesión", use_container_width=True, type="primary"):
        if not email or not password:
            st.error("Por favor completa los campos.")
        else:
            supabase = get_supabase_client()
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if res.user:
                    st.session_state['user'] = {'email': res.user.email, 'id': res.user.id}
                    st.success("Accediendo...")
                    st.rerun()
            except Exception:
                st.error("Credenciales inválidas.")
    
    st.markdown("<div style='margin-top: 2.5rem; border-top: 1px solid #F3F4F6; padding-top: 1.5rem;'>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9CA3AF; font-size: 0.85rem;'>¿No tienes acceso? <br> Consulta con tu administrador PIE.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
