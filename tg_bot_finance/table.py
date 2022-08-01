import openpyxl


def create(name, sname):
    book = openpyxl.load_workbook('finance.xlsx')
    sheet = book.active
    sheet.append(name, sname)

    book.save('finance.xlsx')


