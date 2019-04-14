import cv2
import numpy as np
from PIL import Image, ImageTk
import argparse
import sys

def a():
    image = cv2.imread('Pikachu6.jpg')

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
               image[x,y][2] >= image[x,y][0] + 50:
                image[x,y] = 255,255,255
                liste_rond.append((x,y))
                compteur_rond_rouge += 1

    print(compteur_rond_rouge)


    
 
    return liste_rond



def c(liste_rond):


    image2 = cv2.imread('rond.png')
    
    for i in liste_rond:
        try:
            image2[i[0], i[1]] = 0,0,0
        except:
            pass
    cv2.imwrite("rond.png", image2)




def reconnaissance_rond():

    image = cv2.imread('rond.png')
    print(image.shape[0])

    cerclex = 0
    cercley = 0
    
    liste_rond = []
    
    for x in range(image.shape[0]):
            
        if cerclex >= image.shape[0] - 40:
    
            cerclex = 0
            cercley += 40
            
        if cercley >= image.shape[1] -40:
            break
        
        cercle = cv2.circle(image, (cerclex, cercley), 20, (0, 0, 255), 1)


        cerclex+=40

        
    print(liste_rond)

    cv2.imshow("output transform", image)


    








reconnaissance_rond()


def recolorie_image(self,image):
    pass
#en bleu sinon ca se retrecit



















































































































