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
doc.add_paragraph("this is the first paragraph \n")
style = doc.styles["Normal"]
font = style.font
font.name = "MS Gothic"
font.size = Pt(20)


paragraph1 = doc.add_paragraph("..............11\n")
p1 = paragraph1.add_run("this is the second paragraph!!! \n")
p1.font.size = Pt(48)
p1.font.name = "Arial"

paragraph2 = doc.add_paragraph("............22 \n")
p2 = paragraph2.add_run("this is the third paragraph!!!")
p2.font.size = Pt(72)
p2.font.name = "MS Gothic"



doc.save("writing.docx")
