import cv2
import numpy as np

class traitement_caracteristique:

    def reconnaissance_corps_pikachu(self, image):
        self.image = image
        image = cv2.imread(self.image)

        resultat_corps = []

        print(self.image)

        compteur_couleur_jaune = 0
        
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                if image[x,y][0] <= 85 and\
                   image[x,y][1] >= 160 and\
                   image[x,y][2] >= 150:
                    compteur_couleur_jaune += 1

        resultat_corps.append((self.image, compteur_couleur_jaune))
        print(resultat_corps)

        return resultat_corps


    def reconnaissance_rond(self, image):
        self.image = image
        image = cv2.imread(self.image)
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cimg = cv2.medianBlur(gray, 5)

        circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 2, 100, param1=50,
                                    param2=30, minRadius=40, maxRadius=55)

        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
                cv2.circle(image, (x, y), r, (0, 255, 0), 2)
                cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

        cv2.imshow("output transform", image)
        cv2.waitKey(0)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)







