from openpyxl import workbook, load_workbook
wb = load_workbook('C:/Users/DELL/Desktop/git-test/practice folder/excelFile_new.xlsx')
ws = wb["s1"]
wb.create_sheet("s2")








wb.save('excelFile_new.xlsx')