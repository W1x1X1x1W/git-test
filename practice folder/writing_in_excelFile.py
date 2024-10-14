from openpyxl import workbook, load_workbook
wb = load_workbook('C:/Users/DELL/Desktop/h.xlsx')
ws = wb.active
print(ws['A1'].value)