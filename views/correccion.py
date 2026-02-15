import streamlit as st

def render_correccion():
    # Header from Stitch
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2rem;">
            <div>
                <h1 style="font-size: 2.2rem; font-weight: 600; color: #111827 !important; margin-bottom: 0.3rem;">Corrección Asistida</h1>
                <span style="background: #1D4ED8; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">IA ACTIVA</span>
                <span style="color: #6B7280; font-size: 0.85rem; margin-left: 10px;">Portal del Docente - Chile</span>
            </div>
            <div style="text-align: right;">
                <p style="color: #059669; font-weight: 700; font-size: 1.1rem; margin: 0;">Ahorro estimado: 15 min</p>
                <p style="color: #9CA3AF; font-size: 0.8rem;">Documento: Ensayo_IA_Educacion.pdf</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Student Selector
    st.markdown("""
        <div style="background: #F3F4F6; padding: 12px 20px; border-radius: 8px; margin-bottom: 2rem; display: flex; align-items: center; gap: 15px;">
            <span style="font-weight: 600; color: #374151;">Estudiante:</span>
            <span style="background: white; padding: 4px 12px; border: 1px solid #D1D5DB; border-radius: 4px; color: #111827;">Javier Morales - 4° Medio B</span>
        </div>
    """, unsafe_allow_html=True)

    # Main Layout from Stitch
    col_doc, col_ia = st.columns([0.65, 0.35])

    with col_doc:
        st.markdown("""
            <div style="background: white; border: 1px solid #E5E7EB; border-radius: 8px; min-height: 600px; padding: 3rem; box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05);">
                <h4 style="text-align: center; margin-bottom: 2rem; color: #111827;">Ensayo: Impacto de la IA en la Educación Chilena</h4>
                <div style="color: #374151; font-family: 'Times New Roman', serif; line-height: 1.8; font-size: 1.1rem;">
                    <p style="text-indent: 2rem; margin-bottom: 1.5rem;">
                        La inteligencia artificial ha comenzado a transformar el aula chilena de maneras imprevistas. 
                        Desde la personalización del aprendizaje hasta la automatización de tareas administrativas, 
                        el docente de hoy se enfrenta a un cambio de paradigma...
                    </p>
                    <p style="text-indent: 2rem; margin-bottom: 1.5rem;">
                        Un aspecto fundamental es la equidad. ¿Cómo garantizamos que esta tecnología llegue a las 
                        zonas rurales y no solo a los colegios de la capital? El Ministerio de Educación...
                    </p>
                    <div style="background: #F9FAFB; height: 300px; border: 2px dashed #D1D5DB; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 2rem;">
                         <span style="font-size: 2rem; margin-bottom: 10px;">📄</span>
                         <span style="color: #9CA3AF;">Página 2 del documento escaneado</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_ia:
        st.markdown("""
            <div style="background: white; border: 1px solid #E5E7EB; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-top: 4px solid #1D4ED8;">
                <h4 style="margin-bottom: 1.5rem; color: #111827;">Evaluación Sugerida</h4>
                
                <div style="text-align: center; margin-bottom: 2rem;">
                    <p style="color: #6B7280; font-size: 0.8rem; text-transform: uppercase;">Nota Final Estimada</p>
                    <p style="font-size: 3rem; font-weight: 800; color: #111827; margin: 0;">6.8 <span style="font-size: 1.2rem; color: #9CA3AF; font-weight: 400;">/ 7.0</span></p>
                    <div style="width: 100%; height: 6px; background: #E5E7EB; border-radius: 3px; margin: 10px 0;">
                        <div style="width: 98%; height: 100%; background: #059669; border-radius: 3px;"></div>
                    </div>
                    <p style="color: #059669; font-size: 0.75rem; font-weight: 600;">Confianza de la IA: 98%</p>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <p style="font-weight: 700; font-size: 0.9rem; margin-bottom: 10px;">Desglose por Rúbrica</p>
                    <div style="background: #F9FAFB; padding: 12px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid #059669;">
                        <div style="display: flex; justify-content: space-between;">
                            <span style="font-size: 0.85rem; font-weight: 600;">Argumentación</span>
                            <span style="font-weight: 700;">3.0/3.0</span>
                        </div>
                        <p style="font-size: 0.75rem; color: #6B7280; margin-top: 5px;">Uso de fuentes locales y datos específicos.</p>
                    </div>
                    <div style="background: #F9FAFB; padding: 12px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid #059669;">
                        <div style="display: flex; justify-content: space-between;">
                            <span style="font-size: 0.85rem; font-weight: 600;">Ortografía</span>
                            <span style="font-weight: 700;">1.0/1.0</span>
                        </div>
                        <p style="font-size: 0.75rem; color: #6B7280; margin-top: 5px;">Sin errores detectados.</p>
                    </div>
                </div>

                <div style="background: #EFF6FF; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <p style="font-weight: 700; font-size: 0.85rem; color: #1D4ED8; margin-bottom: 5px;">Retroalimentación Sugerida</p>
                    <p style="font-size: 0.8rem; color: #1E40AF; font-style: italic;">"Excelente manejo de la estructura. Se recomienda profundizar más en la conclusión sobre los desafíos tecnológicos."</p>
                </div>

                <div style="display: flex; gap: 10px;">
                    <button style="flex: 2; background: #1D4ED8; color: white; border: none; padding: 10px; border-radius: 6px; font-weight: 600; cursor: pointer;">Confirmar Nota</button>
                    <button style="flex: 1; background: white; border: 1px solid #D1D5DB; color: #374151; padding: 10px; border-radius: 6px; font-weight: 600; cursor: pointer;">Manual</button>
                </div>
                <p style="text-align: center; color: #1D4ED8; font-size: 0.85rem; margin-top: 15px; cursor: pointer; text-decoration: underline;">Regenerar feedback</p>
            </div>
        """, unsafe_allow_html=True)
