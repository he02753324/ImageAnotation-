#This program reads from excels and create folders recursively
import xlrd
from pathlib import Path

def readExcel():
    #讀取Excel檔建立workbook
    book = xlrd.open_workbook('C:\Image Anotation\ProductInfo.xlsx')

    #建立worksheet
    sheet = book.sheet_by_name('工作表1')

    #將r行0欄的資料存進data list
    data = [sheet.cell_value(r, 0)  for r in range(sheet.nrows)]

    #將數字以外的資料去除
    data = [num for num in data if isinstance(num, (int,float))]   
       
    return data
#迴圈建立資料夾(已存在不影響)
data=readExcel()
for r in data:
  r=int(r) 
  r=str(r)   
  path = Path(r"C:\Image Anotation\ProductImage\\"+r) 
  path.mkdir(exist_ok=True)