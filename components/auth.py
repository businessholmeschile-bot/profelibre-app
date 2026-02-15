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
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 70vh;
        }
        .auth-box {
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: white;
            width: 400px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        st.title("ProfeLibre 🚀")
        st.subheader("Bienvenido de nuevo")
        
        email = st.text_input("Correo electrónico")
        password = st.text_input("Contraseña", type="password")
        
        if st.button("Iniciar Sesión", use_container_width=True):
            supabase = get_supabase_client()
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if res.user:
                    st.session_state['user'] = {'email': res.user.email, 'id': res.user.id}
                    st.success("¡Inicio de sesión exitoso!")
                    st.rerun()
            except Exception as e:
                st.error(f"Error de autenticación: {str(e)}")
        
        st.markdown("---")
        st.caption("¿No tienes cuenta? Contacta a soporte.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
