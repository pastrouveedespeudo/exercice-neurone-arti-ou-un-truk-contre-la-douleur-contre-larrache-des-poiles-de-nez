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

    im = cv2.imread('rond.png')

    liste = []

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            if im[x,y][0] == 0 and im[x,y][1] == 0 and  im[x,y][2] == 0:
                liste.append((x,y))
    print(liste)


    liste2 = []

    c=0
    for i in liste:
        print(liste,liste[c+1][0])
        try:
            if i[0] == liste[c+1][0] and\
               i[0] == liste[c+2][0] and\
               i[0] == liste[c+3][0] and\
               i[0] == liste[c+4][0] and\
               i[0] == liste[c+5][0] and\
               i[0] == liste[c+6][0] and\
               i[0] == liste[c+7][0] and\
               i[0] == liste[c+8][0] and\
               i[0] == liste[c+9][0] and\
               i[0] == liste[c+10][0]:
                liste2.append((liste[c], liste[c+1],
                              liste[c+2],
                              liste[c+3],
                              liste[c+4],
                              liste[c+5],
                              liste[c+6],
                              liste[c+7],
                              liste[c+8],
                              liste[c+9],
                              liste[c+10]))

        except:
            pass

        
        c+=10



    print(liste2)


    cv2.imshow("output transform", im)




#ptetre que ca ca peut donner un truk ca donne un demi cercle du gros cercle qui selon cv2 n'en est pas un...
def reconnaissance_rond():

    im = cv2.imread('rond.png')

    liste = []


    c = 0
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            if im[x,y][0] == 0 and im[x,y][1] == 0 and  im[x,y][2] == 0:
                c+=1
                if c == 10:
                    liste.append((x,y))
            else:
                c = 0



reconnaissance_rond()


def recolorie_image(self,image):
    pass
#en bleu sinon ca se retrecit



















































































































