from openpyxl import load_workbook


def read_number():
    X = []
    table = load_workbook('../number_data.xlsx')
    table_sheet_names = table.sheetnames
    for sheet in range(len(table.sheetnames)):
        X.append([])
        for i in range(5):
            for j in range(7):
                X[len(X) - 1].append(table.get_sheet_by_name(str(table_sheet_names[sheet])).cell(row=j+1, column=i+1).value)
    return X
