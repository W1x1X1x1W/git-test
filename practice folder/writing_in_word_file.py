from docx import Document



doc = Document()

doc.add_heading("fisrt heading", 0)

doc.save("writing.docx")
