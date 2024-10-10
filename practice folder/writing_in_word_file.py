from docx import Document
from docx.shared import Pt



doc = Document()

doc.add_heading("first heading", 0)

p = doc.add_paragraph("examples of writing changes")
p.add_run("\n this text is bold").bold = True
p.add_run("\n this text is italic").italic = True

doc.add_paragraph("create a bullet 1 \n", style="List Bullet")
doc.add_paragraph("create a bullet 2 \n", style="List Bullet")




doc.save("writing.docx")
