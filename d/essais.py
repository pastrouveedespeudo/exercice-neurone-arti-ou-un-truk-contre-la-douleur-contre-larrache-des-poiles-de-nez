import cv2
import numpy as np
from PIL import Image, ImageTk
import argparse
import sys
import imutils
from pylab import *
import sys, cv2


def refond_test_image(image):
    image = cv2.imread('pass')
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = 0,255,0



            
def extraction_rose():
    image = cv2.imread('pikachu9.png')

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
    
    print(compteur_rond_rouge)
    
    for i in liste_rond:
        image[i[0],i[1]] = 255,255,255




    print(image[128,216])
    print(image[129,216])
    print(image[130,216])
    print(image[131,216])
    print(image[132,216])
    print(image[133,216])
    print(image[134,216])
    
    image[126,218:250] = 0,255,0
    

    cv2.startWindowThread()
    cv2.namedWindow("preview")
    cv2.imshow("preview", image)

    cv2.waitKey()
    return liste_rond




def recon(liste):

    print(liste)
    image = cv2.imread('rond2.png')

    for i in liste:
        image[i[0],i[1]] = 255,255,255

    cv2.imshow("output transform", image)
    cv2.imwrite("rond2.png", image)





def contour():
    raw_image = cv2.imread('rond2.png')
    bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    _, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
            contour_list.append(contour)

    cv2.drawContours(raw_image, contour_list,  -1, (0,0,0), 100)

    cv2.imwrite("yo.png", raw_image)


def recup_pts():

    listeee = []
    imageee = cv2.imread('yo.png')
    for x in range(imageee.shape[0]):
        for y in range(imageee.shape[1]):
      
            if imageee[x,y][0] <= 10 and\
               imageee[x,y][1] <= 10 and\
               imageee[x,y][2] <= 10:
                listeee.append((x,y))

    return listeee

def traitement_liste(listeee):
    
    image2 = cv2.imread('ya.png')

    for i in listeee:
        image2[i[0], i[1]] = 0,0,0

    cv2.imshow('dzad.png', image2)
    cv2.imwrite("dzad.png", image2)
    return 'dzad.png'

def detection_rond(nom_image):
    
    img = cv2.imread(nom_image,0)#dzad
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,80,
                            param1=50,param2=20,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if circles:
        return True
    else:
        return False



extraction_rose()
##recon(b)

































































