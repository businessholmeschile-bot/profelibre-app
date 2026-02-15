import streamlit as st
import pandas as pd

def render_students():
    st.title("👥 Gestión de Estudiantes PIE")
    st.write("Administra la nómina de alumnos y sus perfiles de adecuación.")
    
    # Simulation of Student Registry
    students_data = {
        "Nombre": ["Felipe Soto", "Camila Rivas", "Amalia Paz", "Juan Pérez", "Elena Marín"],
        "Curso": ["1° Medio A", "1° Medio A", "1° Medio B", "2° Medio A", "2° Medio C"],
        "Perfil": ["Visual", "Foco", "Comprensión", "Visual", "Foco"],
        "Diagnóstico": ["TEA", "TDAH", "Dificultad Lectora", "TEA", "TDAH"]
    }
    df = pd.DataFrame(students_data)
    
    st.dataframe(df, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Agregar Alumno"):
            st.info("Función de agregar alumno (Próximamente)")
    with col2:
        if st.button("📥 Importar desde Excel"):
            st.info("Función de importación masiva (Próximamente)")
