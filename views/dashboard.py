import streamlit as st

def render_dashboard():
    # Header Section from Stitch
    st.markdown("""
        <div style="margin-bottom: 2rem;">
            <h1 style="font-size: 2.5rem; font-weight: 700; color: #111827 !important; margin-bottom: 0.5rem;">
                Recupera tus tardes. <br><span style="color: #1D4ED8;">La IA corrige contigo.</span>
            </h1>
            <p style="font-size: 1.1rem; color: #6B7280;">Automatiza la creación de rúbricas, guías y la corrección de pruebas estandarizadas en segundos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # KPI Grid - Exactly like Stitch 'ProfeLibre Dashboard'
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <p style="color: #6B7280; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Impacto Mensual</p>
                <p style="color: #111827; font-size: 2.2rem; font-weight: 700; margin: 0.2rem 0;">15 horas</p>
                <p style="color: #059669; font-size: 0.9rem; font-weight: 600;">+12% <span style="color: #9CA3AF; font-weight: 400;">tiempo recuperado</span></p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <p style="color: #6B7280; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Alumnos PIE</p>
                <p style="color: #111827; font-size: 2.2rem; font-weight: 700; margin: 0.2rem 0;">12</p>
                <p style="color: #1D4ED8; font-size: 0.9rem; font-weight: 600;">5 <span style="color: #9CA3AF; font-weight: 400;">nuevos perfiles</span></p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <p style="color: #6B7280; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Evaluaciones</p>
                <p style="color: #111827; font-size: 2.2rem; font-weight: 700; margin: 0.2rem 0;">45</p>
                <p style="color: #059669; font-size: 0.9rem; font-weight: 600;">↑ 8 <span style="color: #9CA3AF; font-weight: 400;">esta semana</span></p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Action Cards
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 16px; border: 1px solid #E5E7EB; height: 100%; transition: all 0.3s ease;">
                <div style="background: #EFF6FF; color: #1D4ED8; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <span style="font-size: 1.4rem;">📝</span>
                </div>
                <h3 style="color: #111827 !important; margin-bottom: 0.8rem;">Generar Evaluación</h3>
                <p style="color: #6B7280; line-height: 1.5; margin-bottom: 1.5rem;">Crea pruebas, guías y rúbricas alineados al curriculum nacional en menos de 2 minutos.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Comenzar →", key="btn_dash_gen", use_container_width=True):
            st.session_state['page'] = 'Generador'
            st.rerun()

    with c2:
        st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 16px; border: 1px solid #E5E7EB; height: 100%;">
                <div style="background: #F0FDF4; color: #15803D; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <span style="font-size: 1.4rem;">🤖</span>
                </div>
                <h3 style="color: #111827 !important; margin-bottom: 0.8rem;">Corregir con IA</h3>
                <p style="color: #6B7280; line-height: 1.5; margin-bottom: 1.5rem;">Sube fotos o PDFs de tus pruebas. Nuestra IA detecta respuestas y calcula notas automáticamente.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Subir archivos", key="btn_dash_corr", use_container_width=True):
            st.session_state['page'] = 'Corrección'
            st.rerun()

    # Activity Table - Premium Style
    st.markdown("<br><h3 style='margin-bottom: 1rem;'>Actividad Reciente</h3>", unsafe_allow_html=True)
    
    # Custom HTML Table for Stitch look
    st.markdown("""
        <table style="width: 100%; border-collapse: separate; border-spacing: 0 8px;">
            <thead>
                <tr style="text-align: left; color: #9CA3AF; font-size: 0.85rem; text-transform: uppercase;">
                    <th style="padding: 1rem;">Documento</th>
                    <th style="padding: 1rem;">Estudiante</th>
                    <th style="padding: 1rem;">Estado</th>
                    <th style="padding: 1rem;">Acción</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: white; border: 1px solid #E5E7EB; border-radius: 8px;">
                    <td style="padding: 1.2rem; border-top: 1px solid #E5E7EB; border-bottom: 1px solid #E5E7EB; border-left: 1px solid #E5E7EB; border-radius: 8px 0 0 8px;"><b>Prueba de Lenguaje - 2°M</b></td>
                    <td style="padding: 1.2rem; border-top: 1px solid #E5E7EB; border-bottom: 1px solid #E5E7EB;">Javier Morales</td>
                    <td style="padding: 1.2rem; border-top: 1px solid #E5E7EB; border-bottom: 1px solid #E5E7EB;"><span style="background: #DCFCE7; color: #166534; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600;">LISTO</span></td>
                    <td style="padding: 1.2rem; border-top: 1px solid #E5E7EB; border-bottom: 1px solid #E5E7EB; border-right: 1px solid #E5E7EB; border-radius: 0 8px 8px 0; color: #1D4ED8; cursor: pointer;">Ver resultados →</td>
                </tr>
            </tbody>
        </table>
    """, unsafe_allow_html=True)
