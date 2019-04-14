import cv2
import numpy as np
from PIL import Image, ImageTk
import argparse
import sys
import imutils
from pylab import *
import sys, cv2



def extraction_rose():
    image = cv2.imread('pikachu5.png')

    compteur_rond_rouge = 0

    liste_rond = []

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
               image[x,y][2] >= 200:
                image[x,y] = 255,255,255
                liste_rond.append((x,y))
                compteur_rond_rouge += 1
    
    print(compteur_rond_rouge)
    
    for i in liste_rond:
        image[i[0],i[1]] = 255,255,255




    print(image[630:410,440])
    image[630,410:450] = 0,255,0
    

        
    cv2.imshow("output transform", image)
    return liste_rond





def recon(liste):

    print(liste)
    image = cv2.imread('rond2.png')

    for i in liste:
        image[i[0],i[1]] = 255,255,255

    cv2.imshow("output transform", image)
    cv2.imwrite("rond2.png", image)




  
extraction_rose()
##recon(b)

































































