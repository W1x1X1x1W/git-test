from openpyxl import Workbook, load_workbook
wb = Workbook()
ws = wb.active

list1 = ['name','job','age']
ws.append(list1)








wb.save('excelFile_new.xlsx')