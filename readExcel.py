# -*- coding: utf-8 -*-
import xlrd

def readExcel(source,sheet):
    #讀取Excel檔建立workbook
    book = xlrd.open_workbook(source)

    #建立worksheet
    sheet = book.sheet_by_name(sheet)

    #將r行0欄的資料存進data list
    datalist = [sheet.cell_value(r, 0)  for r in range(sheet.nrows)]

    #將數字以外的資料去除
    datalist = [num for num in datalist if isinstance(num, (int,float))]   
       
    return datalist