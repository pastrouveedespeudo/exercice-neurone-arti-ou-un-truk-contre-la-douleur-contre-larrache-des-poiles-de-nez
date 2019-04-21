import cv2
import numpy as np
from PIL import Image
import shutil
import os


def nettoyage_image_outils(image, nom, c1, c2, c3):
    
    image = cv2.imread(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = c1, c2, c3
 
    cv2.imwrite(nom, image)





def yoyo(image):
    
    image = cv2.imread(image,0)

    liste = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x,y] > 240:
                liste.append((x,y))
           
    img = cv2.imread('outils1.png')
    for i in liste:
        try:
            img[i[0], i[1]] = 0,0,0
        except:
            pass

    cv2.imwrite('outils1.png', img)



def yaya():
    
    img = cv2.imread('outils1.png')

    liste = []
    liste_x = []

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y][0] == 0 and\
                img[x,y][1] == 0 and\
                img[x,y][2] == 0:
                liste.append(y)
                liste_x.append(x)

    b = max(liste)
    a = max(liste_x)

    im = Image.open('outils1.png')
    im = im.crop((0,0,b,a))
    im.save('outils2.png')


    
def yuyu():

    img = cv2.imread('outils2.png')

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

    im = Image.open('outils3.png')
    im = im.resize((a,b), Image.ANTIALIAS)
    im.save('outils3.png')


    
def yiyi(liste):
    
    img = cv2.imread('outils3.png')

    for i in liste:
        img[i[0],i[1]] = 255,255,255

    cv2.imwrite('outils3.png', img)



def pts_autour_yeux(image, liste):

    img = cv2.imread(image,0)
    imgg = cv2.imread(image)

    path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux"

    h = 10
    w = 15
 
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
 
 
def contour(image, c):

    path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux1"

    raw_image = cv2.imread(image)

    bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    _, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
            contour_list.append(contour)

    cv2.drawContours(raw_image, contour_list,  -1, (255,255,255), 2)

    name = 'crop' + str(c) + '.png'

    cv2.imwrite(name, raw_image)

    shutil.move(name, path)

 
        
def detection_rond(nom_image):
    try:
        img = cv2.imread(nom_image,0)
        img = cv2.medianBlur(img,5)
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,80,
                                param1=50,param2=20,minRadius=0,maxRadius=0)

        circles = np.uint16(np.around(circles))

        nombre = 0
        for i in circles:
            for j in i:
                nombre += 1
                
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(255,0,0),2)

            

        cv2.startWindowThread()
        cv2.namedWindow("preview")
        cv2.imshow("preview", cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return nombre
        
    except:
        print(nom_image)
        return 0


    


def suppression(path):
    os.chdir(path)
    liste = os.listdir()
    for i in liste:
        os.remove(i)



if __name__ == "__main__":
    
    nettoyage_image_outils('outils1.png', 'outils1.png', 0,0,255)
    nettoyage_image_outils('outils2.png', 'outils2.png', 0,0,0)
    nettoyage_image_outils('outils3.png', 'outils3.png', 0,0,0)


    yoyo('pikachu2.jpg')
    yaya()
    liste1 = yuyu()
    yy('pikachu2.jpg')
    yiyi(liste1)
    pts_autour_yeux('pikachu2.jpg', liste1)


    path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux"
    os.chdir(path)
    liste = os.listdir()

    c = 0
    for i in liste:
        contour(i, c)
        c+=1


    path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux1"
    os.chdir(path)
    liste = os.listdir()

    nb_cercle = 0
    for i in liste:
        cercle = detection_rond(i)
        nb_cercle += cercle

    print(nb_cercle)
    
    suppression(r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux1")









