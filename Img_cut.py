from PIL import Image
import readdir
import random

def cut(rootdir,desdir):
 #open id.jpg
    
 #讀取folder and files
 image_list=readdir.read(rootdir)


 for i in image_list:
    count=0
    im=Image.open(i)
    
    #將每張image切割，count為張數
    while(count<10):
    
    
        im =Image.open(i)   
        
        #取得圖片size
        width=im.width
        height=im.height
    
        #設定切割區限制
        ewlimit=width*1/2
        swlimit=width*1/2
    
        ehlimit=height*1/3
        shlimit=height*1/3
    
        #start cordinate(上左)
        xs = random.uniform(0, swlimit)
        ys = random.uniform(0,shlimit)
    
        #end cordinate(右下)
        xe = random.uniform(xs+ewlimit,width)
        ye = random.uniform(ys+ehlimit,height)
        print(height,width,xs,ys,xe,ye)
    
        #切割        
        im2 = im.crop((xs, ys, xe, ye))
        
        #儲存(去副檔名,path轉換)
        cutResult=i.replace('.jpg','')
        cutResult=cutResult.replace(rootdir,desdir)         
        im2.save(cutResult+"_c_"+str(count)+".jpg")
        count=count+1
 print("Done")
 
cut(r'C:\Image Anotation\rawImageCut',r'C:\Image Anotation\rawImageCut')
