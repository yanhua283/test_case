import xlrd

# workbook = xlrd.open_workbook('C:\\Users\\28345\\Desktop\\test_case.xlsx')
#获取sheet
# sheet = workbook.sheet_by_index(0)
# value = sheet.cell_value(1,1)
# # print(value)
#
# for row in range(0,sheet.nrows):
#     for col in range(0,sheet.ncols):
#         print(sheet.cell_value(row,col))

class OperationExcel:
    def __init__(self,path,sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_nrow(self):
        return  self.sheet.nrows

    def get_ncol(self):
        return  self.sheet.ncols

    def get_cell(self,row,col):
        cell_v = self.sheet.cell_value(row,col)
        if cell_v == 'null':
            cell_v=''
        return cell_v



# if __name__ == '__main__':
#     op = OperationExcel('C:\\Users\\28345\\Desktop\\test_case.xlsx')
#     print(op.get_cell(1,1))