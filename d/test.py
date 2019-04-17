import cv2
import numpy as np
from PIL import Image



def refond_test_image(image, nom):
    image = cv2.imread(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = 0,255,0
            
    cv2.imwrite(nom, image)


            
image = cv2.imread('pikachu2.jpg',0)


liste = []
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        if image[x,y] < 240:
            liste.append((x,y))

                
print(liste)


img = cv2.imread('dzadd454.png')
for i in liste:
    try:
        img[i[0], i[1]] = 0,5,255
    except:
        pass
    
cv2.startWindowThread()
cv2.namedWindow("preview")
cv2.imshow("preview", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


refond_test_image('dzadd454.png', 'dzadd454.png')









