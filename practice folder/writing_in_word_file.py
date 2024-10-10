from docx import Document
from docx.shared import Pt



doc = Document()

doc.add_heading("first heading", 0)

p = doc.add_paragraph("examples of writing changes")
p.add_run("\n this text is bold").bold = True
p.add_run("\n this text is italic").italic = True




doc.save("writing.docx")
