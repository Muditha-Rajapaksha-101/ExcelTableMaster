from ExcelTableMaster.ExcelTableMaster import ExcelTableMaster

if __name__ == "__main__":    
    tableMaster = ExcelTableMaster( fileName = "my.xlsx", workSheetIndex = 0, tableName = "data")
    #tableMaster.writeTableRow( dataList = [2 , "nimae" , 12])
    tableMaster.writeUniqueTableRow( keyColumnLetter =  "A" , keyIndexNo = 0, dataList = [66 , "HHH" , 12])
    #print(tableMaster.ValueExist("9" , "A"))
