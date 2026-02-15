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
            padding: 2rem;
            margin-top: 5vh;
        }
        .auth-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 3rem;
            width: 100%;
            max-width: 450px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
            text-align: center;
        }
        .auth-title {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #818CF8, #C084FC);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }
        .auth-subtitle {
            color: #94A3B8;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="auth-title">ProfeLibre 🚀</h1>', unsafe_allow_html=True)
    st.markdown('<p class="auth-subtitle">Recupera tu tiempo docente con IA</p>', unsafe_allow_html=True)
    
    email = st.text_input("Correo electrónico", placeholder="docente@ejemplo.com")
    password = st.text_input("Contraseña", type="password", placeholder="••••••••")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Iniciar Sesión", use_container_width=True, type="primary"):
        if not email or not password:
            st.error("Por favor completa todos los campos.")
        else:
            supabase = get_supabase_client()
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if res.user:
                    st.session_state['user'] = {'email': res.user.email, 'id': res.user.id}
                    st.success("¡Bienvenido, Profe!")
                    st.rerun()
            except Exception as e:
                st.error("Credenciales incorrectas. Revisa tu correo y contraseña.")
    
    st.markdown("<div style='margin-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1.5rem;'>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-size: 0.9rem;'>¿No tienes acceso?<br>Solicítalo a tu dirección académica.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
