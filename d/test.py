import cv2
import numpy as np
from PIL import Image



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



def yiyi(liste):
    
    img = cv2.imread('zazazazaz.png')




    for i in liste:
        img[i[0],i[1]] = 255,255,255

        
    cv2.startWindowThread()
    cv2.namedWindow("preview")
    cv2.imshow("preview", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('zazazazaz.png', img)













#'eazeaze.png'
    

##refond_test_image('zaeeee.png', 'zaeeee.png')
##
##yoyo()
refond_test_image('zazazazaz.png', 'zazazazaz.png')
yaya()
a = yuyu()
yiyi(a)




