from ExcelTableMaster.ExcelTableMaster import ExcelTableMaster

if __name__ == "__main__":    
    tableMaster = ExcelTableMaster( fileName = "data.xlsx", workSheetIndex = 0, tableName = "data")
    tableMaster.writeTableRow( dataList = [3 , "Dave" , 12])
    tableMaster.writeMultipleTableRow( dataList = [[2 , "Sunny" , 12] , [3 , "Nimal" , 35]])
    tableMaster.writeUniqueTableRow( keyColumnLetter =  "A" , keyIndexNo = 0, dataList = [66 , "HHH" , 12])
    tableMaster.writeMultipleUniqueTableRow( keyColumnLetter =  "A" , keyIndexNo = 0, dataList = [[2 , "Sunny" , 12] , [3 , "Nimal" , 35]])
    
    print(tableMaster.ValueExist("9" , "A"))
