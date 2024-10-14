from openpyxl import workbook, load_workbook
wb = load_workbook('C:/Users/DELL/Desktop/h.xlsx')
ws = wb.active
print(wb.sheetnames)

ws['A1'].value = 'Names'
print('he')






wb.save('excelFile_new.xlsx')