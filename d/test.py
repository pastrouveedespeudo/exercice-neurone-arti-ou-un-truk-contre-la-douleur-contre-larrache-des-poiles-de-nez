import cv2
import numpy as np
from PIL import Image
import shutil
""

def refond_test_image(image, nom):
    image = cv2.imread(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = 0,0,0
            
    cv2.imwrite(nom, image)


def yoyo():
    
    image = cv2.imread('pikachu2.jpg',0)


    liste = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x,y] > 240:
                liste.append((x,y))

                    
    print(liste)


    img = cv2.imread('zaeeee.png')
    for i in liste:
        try:
            img[i[0], i[1]] = 0,0,0
        except:
            pass
    cv2.imwrite('zaeeee.png', img)


def yaya():
    img = cv2.imread('zaeeee.png')

    liste = []
    liste_x = []




    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y][0] == 0 and\
                img[x,y][1] == 0 and\
                img[x,y][2] == 0:
                liste.append(y)
                liste_x.append(x)

  
    print(liste)
    b = max(liste)
    a = max(liste_x)

    print(a,b)
    im = Image.open('zaeeee.png')
    im = im.crop((0,0,b,a))
    im.save('zaeeee123.png')


    




def yuyu():
    
    img = cv2.imread('zaeeee123.png')

    liste = []
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            try:
                if img[x,y][0] == 0 and\
                    img[x,y][1] == 0 and\
                    img[x,y][2] == 255:
                    if img[x,y+1][0] == 0 and\
                     img[x,y+1][1] == 0 and\
                     img[x,y+1][2] == 0 and\
                     img[x,y+10][0] == 0 and\
                     img[x,y+10][1] == 0 and\
                     img[x,y+10][2] == 255 and\
                     img[x,y-10][0] == 0 and\
                     img[x,y-10][1] == 0 and\
                     img[x,y-10][2] == 255 and\
                     img[x+10,y][0] == 0 and\
                     img[x+10,y][1] == 0 and\
                     img[x+10,y][2] == 255 and\
                     img[x-10,y][0] == 0 and\
                     img[x-10,y][1] == 0 and\
                     img[x-10,y][2] == 255:
                         liste.append((x,y))

            except:
                pass

    

    return liste




def yy(image):

    im_base = Image.open(image)

    a = im_base.width
    b = im_base.height

    print(a,b)

    im = Image.open('zazazazaz.png')
    im = im.resize((a,b), Image.ANTIALIAS)
    im.save('zazazazaz.png')

    





def yiyi(liste):
    
    img = cv2.imread('zazazazaz.png')

    for i in liste:
        img[i[0],i[1]] = 255,255,255

    print(liste)


    cv2.imwrite('zazazazaz.png', img)
    print('fin')

    
def superposition(image):

    p1 = Image.open(image)
    p2 = Image.open('zazazazaz.png')
    p3 = Image.blend(p1, p2, 1)
    p3.save('super.jpg')



def pts_autour_yeux(image, liste):

    img = cv2.imread(image,0)
    imgg = cv2.imread(image)

    path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux"

    h = 10
    w = 15
 
    print(liste)
    
    c = 0
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            
            for i in liste:

                if x == i[0] and y == i[1]:
                    crop_img = img[y-10:y+10+h, x-10:x+10+w]

                    name = "crop" + str(c) + ".png"
                    cv2.imwrite(name, crop_img)
                    shutil.move(name, path)

                          
                    c+=1       
 
                


    #imgg[120:130, 116] = 0,0,255
    
    cv2.startWindowThread()
    cv2.namedWindow("preview")
    cv2.imshow("preview", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def detection_yeux():
    pass

def suppression_yeux():
    pass








#'eazeaze.png'

##refond_test_image('zaeeee.png', 'zaeeee.png')
##
##yoyo()
refond_test_image('zazazazaz.png', 'zazazazaz.png')
yaya()
a = yuyu()
yy('pikachu2.jpg')
yiyi(a)
superposition('pikachu2.jpg')
pts_autour_yeux('pikachu2.jpg', a)


