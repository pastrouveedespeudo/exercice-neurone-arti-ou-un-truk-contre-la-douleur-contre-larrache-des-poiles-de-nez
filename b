import numpy as np
from PIL import Image
import cv2
import os

#tenserflow veut pas s'installer alors nique


class traitement_image:

    def fichier(self):
        os.chdir(r"C:\Users\jeanbaptiste\reso\image")
        liste = os.listdir
        return liste

    def recadra(self, liste):
        self.liste = liste

        for i in self.liste:
            pass


class image_un:


    def ouverture(self, image):
        self.image = image
        
        img = cv2.imread(self.image)

        return img


    def cherche_droite_verticale(self, image):
        self.image = image
        
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                if (self.image[x:x+100,y] == np.array([0,0,0])).all():
                    print(x,y)
                    return "droite verticale"


    def cherche_droite_en_diagonale(self, image):
        pass
        #for i in range(50):
            #x+i, y-i



    def cherche_aisselle_un(self, image):
        pass

    def cherche_les_trois_fermeture_un(self, image):
        pass

    def cherche_les_rectangle_du_un(self, image):
        self.image = image

        rectangle_verticale = []
        
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                if (self.image[x,y] == np.array([0,0,0])).all():
                    rectangle_verticale.append((x,y))

        maximum = max(rectangle_verticale)
        minimum = min(rectangle_verticale)
        
        if self.image([minimum[0]:maximum[0],minimum[1]:maximum[1]] = np.array[0,0,0]).all():
            return "rectangle vertical"
        

    def cherche_droite_un_mal_dessiner(self,image):
        pass

    
    def montre(self, image):
        self.image = image
        cv2.imshow("yo.jpg", self.image)



class poids:
    pass


if __name__ == "__main__":


    
    l_image = "1.jpg"

    img = image_un()
    image1 = img.ouverture(l_image)
    
    img.cherche_droite_verticale(image1)
    img.cherche_les_rectangle_du_un(image1)
    img.cherche_droite_en_diagonale(image1)
    
    img.montre(image1)
















    
