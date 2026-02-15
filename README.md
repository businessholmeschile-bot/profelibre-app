# ProfeLibre 🚀 

**Automatización de Adecuaciones Curriculares (PIE) para el Docente Chileno.**

ProfeLibre es una plataforma SaaS diseñada específicamente para profesores de enseñanza media en Chile. Su objetivo es transformar evaluaciones estándar en versiones adaptadas para necesidades educativas especiales, aplicando lógica pedagógica avanzada y automatizando tareas administrativas para devolver tiempo valioso al docente.

## ✨ Características Principales
- **Core Engine V13.2**: Procesamiento inteligente de documentos Word, PDF, Imágenes (OCR) y Google Docs.
- **Lógica de Enroque**: Manipulación automática de distractores y alternativas basada en claves de corrección.
- **Perfiles Especializados**: Generación de documentos adaptados para perfiles específicos:
  - **Felipe (Visual)**: Optimización de interlineado y diseño.
  - **Camila (Foco)**: Destacado de verbos imperativos.
  - **Amalia (Comprensión)**: Inserción de glosarios y pausas de lectura.
- **Integración Real**: Autenticación segura mediante Supabase.
- **Dashboard de Métricas**: Visualización del tiempo docente ahorrado.

## 🛠️ Stack Tecnológico
- **Frontend/Backend**: [Streamlit](https://streamlit.io/) (Python)
- **Base de Datos & Auth**: [Supabase](https://supabase.com/)
- **Procesamiento Documental**: `python-docx`, `pdfplumber`, `pytesseract`
- **Despliegue**: Vercel

## 🚀 Instalación y Desarrollo Local
1. Clonar el repositorio.
2. Crear un entorno virtual: `python3 -m venv venv`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar secretos en `.streamlit/secrets.toml`.
5. Ejecutar la aplicación: `streamlit run main.py`

## 🔒 Licencia y Derechos
**Propiedad de ProfeLibre.**  
Copyright © 2026. Todos los derechos reservados. El código código contenido en este repositorio es propietario y no se permite su uso, distribución o modificación sin autorización expresa.

---
*Diseñado con ❤️ para la educación chilena.*
