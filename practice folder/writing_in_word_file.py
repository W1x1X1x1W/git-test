from docx import Document
from docx.shared import Pt



doc = Document()
'''add heading text'''

doc.add_heading("first heading", 0)

'''add paragraphs'''
p = doc.add_paragraph("examples of writing changes")
p.add_run("\n this text is bold").bold = True
p.add_run("\n this text is italic").italic = True

doc.add_paragraph("create a bullet 1 \n", style="List Bullet")
doc.add_paragraph("create a bullet 2 \n", style="List Bullet")

'''add paraghraph with diifernt font and size for every paragraph'''

style = doc.styles["Normal"]
font = style.font
font.name = "MS Gothic"
font.size = Pt(20)


paragraph1 = doc.add_paragraph("..............")
p1 = paragraph1.add_run("this is the seconde paragraph!!!")
p1.font.size = Pt(72)



doc.save("writing.docx")
