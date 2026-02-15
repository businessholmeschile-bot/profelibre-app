import streamlit as st

def render_landing():
    # Hero Section
    st.markdown("""
        <div style="text-align: center; padding: 4rem 1rem; margin-bottom: 2rem;">
            <h1 style="font-size: 3.5rem; font-weight: 800; color: #111827; line-height: 1.1;">
                Recupera tus tardes. <br><span style="color: #1D4ED8;">La IA corrige contigo.</span>
            </h1>
            <p style="font-size: 1.4rem; color: #4B5563; max-width: 800px; margin: 1.5rem auto;">
                Automatiza la creación de rúbricas, guías y la corrección de pruebas estandarizadas en segundos. 
                Ahorra hasta 15 horas al mes en burocracia docente.
            </p>
            <div style="margin-top: 2.5rem; display: flex; justify-content: center; gap: 1rem;">
                <button class="stButton" onclick="window.location.href='#planes'" style="background-color: #1D4ED8; color: white; padding: 0.8rem 2rem; border-radius: 8px; border: none; font-weight: 600; cursor: pointer;">
                    Ver Planes
                </button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("<h2 style='text-align: center; margin-bottom: 3rem;'>¿Qué puedes hacer con ProfeLibre?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style="background: white; padding: 2.5rem; border-radius: 12px; border: 1px solid #E5E7EB; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                <div style="background: #EFF6FF; width: 50px; height: 50px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <span style="font-size: 1.5rem;">📝</span>
                </div>
                <h3 style="color: #111827; margin-bottom: 1rem;">Generador de Evaluaciones</h3>
                <p style="color: #6B7280; line-height: 1.6;">Crea pruebas, guías y rúbricas alineados al curriculum nacional en menos de 2 minutos.</p>
                <p style="color: #1D4ED8; font-weight: 600; margin-top: 1.5rem; cursor: pointer;">Comenzar →</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style="background: white; padding: 2.5rem; border-radius: 12px; border: 1px solid #E5E7EB; height: 100%; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                <div style="background: #EFF6FF; width: 50px; height: 50px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <span style="font-size: 1.5rem;">🤖</span>
                </div>
                <h3 style="color: #111827; margin-bottom: 1rem;">Corrección con IA</h3>
                <p style="color: #6B7280; line-height: 1.6;">Sube fotos o PDFs de tus pruebas. Nuestra IA detecta respuestas y calcula notas automáticamente.</p>
                <div style="margin-top: 1.5rem; display: flex; align-items: center; gap: 0.5rem; color: #1D4ED8; font-weight: 600;">
                    <span>☁️ Subir archivos</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Pricing Section
    st.markdown("<div id='planes' style='padding-top: 100px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin: 4rem 0;">
            <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">Planes diseñados para el docente moderno</h2>
            <p style="color: #6B7280; font-size: 1.1rem;">Automatiza tus evaluaciones y correcciones con IA estandarizada.</p>
        </div>
    """, unsafe_allow_html=True)
    
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 12px; border: 1px solid #E5E7EB; text-align: center;">
                <h4 style="color: #6B7280;">Plan Gratuito</h4>
                <p style="font-size: 2.5rem; font-weight: 800; margin: 1rem 0;">$0</p>
                <ul style="text-align: left; color: #6B7280; margin: 1.5rem 0; list-style: none; padding: 0;">
                    <li>✓ 3 evaluaciones al mes</li>
                    <li>✓ Herramientas básicas</li>
                    <li>✓ Soporte por email</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Empezar Gratis", key="btn_free", use_container_width=True):
            st.session_state['show_login'] = True
            st.rerun()

    with p2:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 12px; border: 2px solid #1D4ED8; text-align: center; position: relative;">
                <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #1D4ED8; color: white; padding: 2px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">RECOMENDADO</div>
                <h4 style="color: #1D4ED8;">Plan Pro Anual</h4>
                <p style="font-size: 2.5rem; font-weight: 800; margin: 1rem 0;">$10.490 <span style="font-size: 1rem; font-weight: 400; color: #6B7280;">/mes</span></p>
                <ul style="text-align: left; color: #6B7280; margin: 1.5rem 0; list-style: none; padding: 0;">
                    <li>✓ Evaluaciones ilimitadas</li>
                    <li>✓ Todo lo del Plan Pro</li>
                    <li>✓ Acceso anticipado a IA</li>
                    <li>✓ Planificación semanal</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Elegir Plan Anual", key="btn_annual", use_container_width=True, type="primary"):
            st.session_state['show_login'] = True
            st.rerun()

    with p3:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 12px; border: 1px solid #E5E7EB; text-align: center;">
                <h4 style="color: #6B7280;">Plan Pro Mensual</h4>
                <p style="font-size: 2.5rem; font-weight: 800; margin: 1rem 0;">$12.990 <span style="font-size: 1rem; font-weight: 400; color: #6B7280;">/mes</span></p>
                <ul style="text-align: left; color: #6B7280; margin: 1.5rem 0; list-style: none; padding: 0;">
                    <li>✓ Evaluaciones ilimitadas</li>
                    <li>✓ Soporte prioritario</li>
                    <li>✓ Exportación premium</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Suscribirse Pro", key="btn_monthly", use_container_width=True):
            st.session_state['show_login'] = True
            st.rerun()

    # Footer
    st.markdown("""
        <div style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid #E5E7EB; text-align: center; color: #9CA3AF;">
            <p>ProfeLibre 2026 - Herramienta de automatización pedagógica diseñada para docentes en Chile.</p>
        </div>
    """, unsafe_allow_html=True)

    # Login Float Option
    with st.sidebar:
        st.markdown("### ¿Ya eres usuario?")
        if st.button("Iniciar Sesión Docente", use_container_width=True):
            st.session_state['show_login'] = True
            st.rerun()
