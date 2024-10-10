from docx import Document
from docx.shared import Pt


doc = Document()

doc.add_heading("fisrt heading", 0)

doc.save("writing.docx")
