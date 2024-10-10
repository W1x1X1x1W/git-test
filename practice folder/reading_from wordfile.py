from docx.api import Document


doc = Document("test1.docx")

for p in doc.paragraphs:
    if p.style.name.startswith("Heading") or p.style.name == "Title":
        print(p.text)


for table in doc.tables:
    print("new table")
    for row in table.rows :
        print("|".join(cell.text for cell in row.cells))