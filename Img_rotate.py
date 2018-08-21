#This program rotate images and save them
import readdir
from PIL import Image
import random
def rotate(rootdir,desdir):
 #讀取folder and files
 image_list=readdir.read(rootdir)


 for i in image_list:
    count=0
    im=Image.open(i)
    
    #將每張image旋轉，count為張數
    while(count<10):
        
        #旋轉 (angle(隨機浮點數),resample,expand)
        im2=im.rotate(random.uniform(0,360),0,1)
        
        #去除.jpg 副檔名
        rResult=i.replace('.jpg','')
        
        #將source替換成destination
        rResult=rResult.replace(rootdir,desdir)
        
        #儲存  
        count+=1
        im2.save(rResult+"_r_"+str(count)+".jpg")
 print("Done")
   
rotate(r'C:\Image Anotation\rawImageCut',r'C:\Image Anotation\rawImageCut')        
        
