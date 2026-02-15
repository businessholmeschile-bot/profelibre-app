from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
import os
import io
import zipfile
import pypdf
import requests

class CoreEngineV13:
    def __init__(self, roster_data=None, logo_img=None):
        """
        roster_data: List of dicts with keys 'Nombre', 'Perfil', etc.
        """
        self.roster_data = roster_data if roster_data else []
        self.logo_img = logo_img
        self.extracted_text = ""

    def load_source(self, source_file, file_type):
        """Loads and extracts text from various sources."""
        if file_type == 'docx':
            doc = Document(source_file)
            self.extracted_text = "\n".join([p.text for p in doc.paragraphs])
        elif file_type == 'pdf':
            reader = pypdf.PdfReader(source_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            self.extracted_text = text
        elif file_type in ['png', 'jpg', 'jpeg']:
            self.extracted_text = "[OCR no disponible en esta versión ligera. Por favor usa archivos Word o PDF.]"
        elif file_type == 'google_url':
            self.extracted_text = "[Integración Google: Descargando contenido de la URL...]\n" + self._handle_google_export(source_file)
        
        return self.extracted_text

    def _handle_google_export(self, url):
        """Helper to handle Google Docs export URLs."""
        try:
            if "docs.google.com/document" in url:
                export_url = url.split('/edit')[0] + '/export?format=txt'
                response = requests.get(export_url)
                return response.text
            return "Formato de URL no soportado directamente. Por favor usa la opción de exportar a PDF."
        except:
            return "Error al acceder a la URL de Google Docs."

    def standardize_document(self, doc):
        """Standardizes font to Calibri 11pt and sets up the invisible header."""
        for section in doc.sections:
            header = section.header
            header.is_linked_to_previous = False
            for p in header.paragraphs:
                p.text = ""
            
            table = header.add_table(1, 2, width=Inches(6.5))
            table.autofit = False
            
            cell_logo = table.cell(0, 0)
            if self.logo_img:
                run = cell_logo.paragraphs[0].add_run()
                logo_stream = io.BytesIO(self.logo_img)
                run.add_picture(logo_stream, width=Inches(1))
            
            cell_text = table.cell(0, 1)
            p = cell_text.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = p.add_run("EVALUACIÓN ESTANDARIZADA")
            run.font.name = 'Calibri'
            run.font.size = Pt(14)
            run.font.bold = True

        for p in doc.paragraphs:
            for run in p.runs:
                run.font.name = 'Calibri'
                run.font.size = Pt(11)

    def apply_enroque_logic(self, doc, matrix_data, no_borrar_d=False):
        """
        matrix_data: list of dicts with correct keys.
        """
        if no_borrar_d:
            return

        paragraphs = list(doc.paragraphs)
        for i, p in enumerate(paragraphs):
            text = p.text.strip()
            if text.startswith("D)") or text.startswith("D."):
                p.text = "" # Simplified distractor removal

    def apply_profile_specialization(self, doc, profile_name):
        """Applies specific styling based on student profiles."""
        if profile_name == "Visual":
            for p in doc.paragraphs:
                p.paragraph_format.line_spacing = 1.5
        
        elif profile_name == "Foco":
            imperatives = ["Analiza", "Calcula", "Determina", "Explica", "Identifica", "Lee", "Observa", "Responde"]
            for p in doc.paragraphs:
                for run in p.runs:
                    for verb in imperatives:
                        if verb in run.text:
                            run.font.bold = True
                            run.font.underline = True
        
        elif profile_name == "Comprensión":
            p_gloss = doc.paragraphs[0].insert_paragraph_before("GLOSARIO DE TÉRMINOS")
            p_gloss.runs[0].font.bold = True
            p_gloss.runs[0].font.size = Pt(12)
            
            count = 0
            original_paragraphs = list(doc.paragraphs)
            for i, p in enumerate(original_paragraphs):
                if len(p.text.strip()) > 20:
                    count += 1
                    if count % 4 == 0:
                        pause = p.insert_paragraph_after("[PAUSA DE LECTURA - Tómate un momento para reflexionar]")
                        pause.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        run = pause.runs[0]
                        run.font.italic = True
                        run.font.size = Pt(10)

    def generate_all(self, selected_students, matrix_data, source_file=None):
        """
        selected_students: List of dicts.
        matrix_data: List of dicts.
        """
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            for student in selected_students:
                if source_file and hasattr(source_file, 'seek'):
                    source_file.seek(0)
                    doc = Document(source_file)
                else:
                    doc = Document()
                    doc.add_paragraph(self.extracted_text)
                
                self.standardize_document(doc)
                no_borrar_d = student.get('No borrar D', False)
                self.apply_enroque_logic(doc, matrix_data, no_borrar_d)
                self.apply_profile_specialization(doc, student['Perfil'])
                
                filename = f"Adecuacion_{student['Nombre']}_{student['Perfil']}.docx"
                doc_io = io.BytesIO()
                doc.save(doc_io)
                zip_file.writestr(filename, doc_io.getvalue())
        
        return zip_buffer.getvalue()
