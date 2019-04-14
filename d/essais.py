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

b = a()

def c(liste_rond):


    print(liste_rond)




c(b)












def reconnaissance_rond(liste):

    image = cv2.imread('rond.png')


    cv2.imshow("output transform", image)


    








#reconnaissance_rond()


def recolorie_image(self,image):
    pass
#en bleu sinon ca se retrecit



















































































































