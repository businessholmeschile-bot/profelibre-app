import streamlit as st

def render_students():
    st.title("👥 Gestión de Estudiantes PIE")
    st.write("Administra la nómina de alumnos y sus perfiles de adecuación.")
    
    # Simulation of Student Registry (using a list of dicts instead of pandas)
    students_data = [
        {"Nombre": "Felipe Soto", "Curso": "1° Medio A", "Perfil": "Visual", "Diagnóstico": "TEA"},
        {"Nombre": "Camila Rivas", "Curso": "1° Medio A", "Perfil": "Foco", "Diagnóstico": "TDAH"},
        {"Nombre": "Amalia Paz", "Curso": "1° Medio B", "Perfil": "Comprensión", "Diagnóstico": "Dificultad Lectora"},
        {"Nombre": "Juan Pérez", "Curso": "2° Medio A", "Perfil": "Visual", "Diagnóstico": "TEA"},
        {"Nombre": "Elena Marín", "Curso": "2° Medio C", "Perfil": "Foco", "Diagnóstico": "TDAH"}
    ]
    
    st.table(students_data)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Agregar Alumno"):
            st.info("Función de agregar alumno (Próximamente)")
    with col2:
        if st.button("📥 Importar desde Excel"):
            st.info("Función de importación masiva (Próximamente)")
