#This program read folders and files recursively
from os import walk
from os.path import  join

def read(path):
    # 指定要列出所有檔案的目錄
    rootpath = path
    namelist=[]
    
  
    # 遞迴列出所有檔案的絕對路徑
    for root, dirs, files in walk(rootpath):
        for f in files:
            fullpath = join(root, f)
            
            #把路徑存入list
            namelist.append(fullpath)
            
    return namelist
           

