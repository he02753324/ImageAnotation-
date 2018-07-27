#This program rotate images and save them
import readdir
from PIL import Image

#讀取folder and files
image_list=readdir.read(r'C:\Image Anotation\rawImageCut')


for i in image_list:
    count=0
    im=Image.open(i)
    while(count<2):
        #旋轉
        im2=im.rotate(60)
        #去除.jpg 副檔名
        rResult=i.replace('.jpg','')
    
        #儲存  
        count+=1
        im2.save(rResult+"r"+str(count)+".jpg")
        
        