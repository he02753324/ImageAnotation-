#This program reads from excels and create folders recursively
import readExcel
from pathlib import Path

def mkdir(source,sheet,desdir):
 datalist=readExcel.readExcel(source,sheet)
 #迴圈建立資料夾(已存在不影響)
 #r是資料夾名稱
 for r in datalist:
    
  r=int(r) 
  r=str(r)
  desdir=desdir+r
  
  path = Path(desdir) 
  path.mkdir(exist_ok=True)

mkdir('C:\Image Anotation\ProductInfo.xlsx',"工作表1",r"C:\Image Anotation\rawImageCut\\")
