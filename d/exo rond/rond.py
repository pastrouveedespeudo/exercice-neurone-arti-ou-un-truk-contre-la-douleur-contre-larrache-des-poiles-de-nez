from cv2 import *
import numpy as np
from cv2.cv2 import *

def un():
    
    im = cv2.imread('rond.png',0)

    liste = []
    liste_x = []

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            if im[x,y] == 0:
                liste.append((x,y))
                liste_x.append(x)
                
                
    return liste, liste_x



def trois(liste, liste1):
    print(liste)

    a = liste[0]
    b = liste[-1]
    print(a,b)

    c = a + b 
    d = c /2
    print(d)
    
    liste_pts = []

    pts1 = [i for i in liste1 if i[0] == a]


    print(pts1[0][1],'00')
    #d = centre, pts = y
    return d, pts1[0][1]

def deux(liste, centre, y):

    print(centre, y)
    
    im = cv2.imread('ronron1.png')
    for i in liste:
        im[i[0], i[1]] = 0,0,0

        
    im[int(centre):int(centre) + 10,int(y)] = 0,0,255
    im[int(centre)-10:int(centre), int(y)] = 0,0,255
    im[int(centre), int(y):int(y)+10] = 0,0,255
    im[int(centre), int(y)-10:int(y)] = 0,0,255
 
 
    cv2.imshow('dzadza', im)




































if __name__ == "__main__":
    
    liste = un()
    pts = trois(liste[1], liste[0])
    deux(liste[0], pts[0], pts[1])
    

















