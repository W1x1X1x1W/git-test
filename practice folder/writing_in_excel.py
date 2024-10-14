from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
wb = Workbook()
ws = wb.active
ws.title = 'sh1'

for row in range(1,7):
    for col in range(1,4):
        char = get_column_letter(col)
        ws[char + str(row)].value = char + str(row)

ws.insert_rows(2)
ws.delete_rows(2)
ws.insert_cols(2)
ws.delete_cols(2)

ws.move_range("A1:C3", rows = 3, cols = 5)












wb.save('excelFile_new.xlsx')