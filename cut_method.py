# -*- coding: utf-8 -*-

from PIL import Image
def cut(id,vx,vy):
    #open id.jpg
  
    source = "C:/Users/456470/Desktop/Image cut/"+ id + ".jpg"
    cut = "C:/Users/456470/Desktop/Image cut/"+ id +"_cut_"
    im =Image.open(source)

    #shift value
    dx = 300
    dy = 200
    n = 1

    #start from up-left
    xs = 0
    ys = 0
    xe = vx
    ye = vy

    #x-cut
    while xe <= 5312:
        #y-cut
        while ye <= 2988:
            cutResult = cut + str(n) + ".jpg"
            #print (n,xs,ys,xe,ye)
            im2 = im.crop((ys, xs, ye, xe))
            im2.save(cutResult)
            ys = ys + dy
            ye = ye + vy
            n = n + 1
        xs = xs + dx
        xe = xe + vx
        ys=0
        ye=vy
       
       
cut("Desert",300,200)