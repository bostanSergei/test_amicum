import xlsxwriter


col_name = [["A", 'version'], ["B", 'release date'], ["C", 'download link'], ["D", 'notes link']]
work_book = xlsxwriter.Workbook("python_versions.xlsx")
work_sheet = work_book.add_worksheet()

for index in range(len(col_name)):
    work_sheet.write(f"{col_name[index][0]}1", col_name[index][1])

work_book.close()