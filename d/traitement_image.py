import cv2
import numpy as np


def corps_pikachu(image):

    img = cv2.imread(image)

    resultat_corps = []
    yo = []
    compteur_couleur_jaune = 0
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y][0] <= 85 and\
               img[x,y][1] >= 160 and\
               img[x,y][2] >= 150:
                compteur_couleur_jaune += 1
                yo.append((x,y))

    resultat_corps.append((image, compteur_couleur_jaune))


    for i in yo:
        img[i[0],i[1]] = 0,0,255
    

    return resultat_corps



def traitement(image, liste):

    img = cv2.imread(image)

    a = img.shape[1]
    b = img.shape[0]
    c = a * b

    pourcentage = 100*int(liste) / c

    return pourcentage




if __name__ == "__main__":

    liste1 = corps_pikachu('Pikachu2.jpg')
    traitement(liste1[0][0], liste1[0][1])

