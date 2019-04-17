import cv2
import numpy as np
from PIL import Image, ImageTk
import argparse
import sys
import imutils
from pylab import *
import sys, cv2


def refond_test_image(image, nom):
    image = cv2.imread(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = 0,255,0


    cv2.imwrite(str(nom), image)
    
def refond_test_image2(image, nom):
    image = cv2.imread(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = 255,255,255
            

    cv2.imwrite(str(nom), image)
            
def extraction_rose(image):
    image = cv2.imread(image)

    compteur_rond_rouge = 0

    liste_rond = []
    #un des truk les plus chiant de ma vie
    
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x,y][2] >= image[x,y][1] + 50 and\
               image[x,y][2] >= 150 and\
               image[x,y][1] <= 160 and\
               image[x,y][1] >= 50 and\
               image[x,y][0] >= 50 and\
               image[x,y][0] <= 145 and\
               image[x,y][2] >= image[x,y][0] + 50 or\
               image[x,y][2] >= 200 and\
               image[x,y][0] <= 50 and\
               image[x,y][1] <= 50 or\
               image[x,y][2] >= 200 and\
               image[x,y][1] <= 48 and\
               image[x,y][0] <= 55 or\
               image[x,y][2] >= 200 and\
               image[x,y][1] <= 32 and\
               image[x,y][0] <= 57 or\
               image[x,y][0] <= 130 and\
               image[x,y][1] <= 70 and\
               image[x,y][2] >= 200 or\
               image[x,y][0] <= 49 and\
               image[x,y][1] <= 90 and\
               image[x,y][2] >= 230 or\
               image[x,y][0] <= 45 and\
               image[x,y][1] <= 53 and\
               image[x,y][2] >= 160 and\
               image[x,y][2] > image[x,y][0] + 100 and\
               image[x,y][2] > image[x,y][1] + 100 or\
               image[x,y][0] <= 50 and\
               image[x,y][1] <= 60 and\
               image[x,y][2] >= 160 or\
               image[x,y][0] <= 45 and\
               image[x,y][1] <= 50 and\
               image[x,y][2] >= 150 or\
               image[x,y][0] <= 25 and\
               image[x,y][1] <= 70 and\
               image[x,y][2] >= 150 or\
               image[x,y][0] <= 30 and\
               image[x,y][1] <= 90 and\
               image[x,y][2] >= 160 and\
               image[x,y][2] > image[x,y][1] + 60 and\
               image[x,y][2] > image[x,y][0] + 140 or\
               image[x,y][0] <= 30 and\
               image[x,y][1] <= 90 and\
               image[x,y][2] >= 160 or\
               image[x,y][0] <= 50 and\
               image[x,y][1] <= 60 and\
               image[x,y][2] >= 130 or\
               image[x,y][0] <= 10 and\
               image[x,y][1] <= 45 and\
               image[x,y][2] >= 120:

                image[x,y] = 255,255,255
                liste_rond.append((x,y))
                compteur_rond_rouge += 1
    

    for i in liste_rond:
        image[i[0],i[1]] = 255,255,255

    return liste_rond


def recon(liste):

    image = cv2.imread('rond2.png')

    print(liste)

    for i in liste:
        image[i[0],i[1]] = 255,255,255

    cv2.imwrite("rond2.png", image)

    return liste


def nettoyage1(liste):


    liste1 = []
    c = 0
    for i in liste[:-2]:
        if i[1] + 1 == liste[c+1][1]:
            liste1.append(i)
        
        c+=1

    return liste1

def nettoyage2(liste):
 
    
    liste2 = []
    c = 0
    for i in liste[:-2]:
        if i[1] + 1 == liste[c+1][1] and\
           i[0] == liste[c+1][0]:
            liste2.append(i)
        c+=1
        
    return liste2

def nettoyage3(liste2):

    b = [[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[],[]]



    liste3 = []

    c = 0
    d = 0

    for i in liste2[:-2]:
     
        if i[0] == liste2[c + 1][0] and\
           i[1] + 1 == liste2[c + 1][1]:
            b[d].append(i)
        else:
            d+=1
        
        c+=1

    y = []
    for i in b:
        if i == []:
            pass
        else:
            if len(i) <= 9:
                pass
            else:
                y.append(i)

    return y



def nettoyage4(y):

    c = 0
    d = 0
    yy = []
    aze = []

    for i in y:
        for j in i:
            yy.append(j)

        c+=1
        
    for i in yy:
        aze.append(i[1])
            
    aze = set(aze)
    aze = list(aze)
    aze.sort()
    print(aze)

    image = cv2.imread('rond2.png')
    
    yoo = [[],[],[]]

    c=0
    d =0
    for i in aze:
        try:
            if i + 1 != aze[c + 1]:
                d+=1
            else:
                yoo[d].append(i)
        except:
            pass
        c+=1

    oo = []
    a = ""

    for i in yy:
        a = ""
        for j in yoo[1]:
            if j == i[1]:
                a = True

        if a == True:
            pass
        else:
            image[i[0],i[1]] = 255,255,255

    cv2.imwrite("image_rond_pika.png", image)

    

    cv2.destroyAllWindows()


def contour(image):
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

    cv2.drawContours(raw_image, contour_list,  -1, (0,0,0), 60)


    cv2.startWindowThread()
    cv2.namedWindow("preview")
    cv2.imshow("preview", raw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("yo.png", raw_image)




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
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

            

        cv2.startWindowThread()
        cv2.namedWindow("preview")
        cv2.imshow("preview", cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return nombre

    except:
        return '0 rond'


refond_test_image('rond2.png', 'rond2.png')
refond_test_image('yo.png', 'yo.png')
refond_test_image2('ya.png', 'ya.png')
refond_test_image2('dzad.png', 'dzad.png')

extra = extraction_rose('pikachu1.jpg')

b = nettoyage1(extra)
c = nettoyage2(b)
d = nettoyage3(c)
e = nettoyage4(d)

contour("image_rond_pika.png")
rond = detection_rond("yo.png")

print(rond)










































































