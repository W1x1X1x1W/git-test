from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
wb = load_workbook('excelFile_new.xlsx')
ws = wb.active
ws.title = 'sh1'

for row in range(1,7):
    for col in range(1,4):
        char = get_column_letter(col)
        ws[char + str(row)].value = char + str(row)

ws.merge_cells("A1:D1")









wb.save('excelFile_new.xlsx')