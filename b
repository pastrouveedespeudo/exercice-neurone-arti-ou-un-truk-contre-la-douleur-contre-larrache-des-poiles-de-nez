
from PIL import Image
import cv2
import os

#tenserflow veut pas s'installer alors nique


class traitement_image:

    def fichier(self):
        os.chdir("C:\Users\jeanbaptiste\reso\image")
        liste = os.listdir
        return liste

    def recadra(self, liste):
        self.liste = liste

        for i in self.liste:
            pass


class image:


    def ouverture(self, image):
        self.image = image
        
        img = cv2.imread(self.image)

        return img


    def entree_un_un(self, image):
        self.image = image

        for x in range(-self.image.shape[0]):
            for y in range(-self.image.shape[1]):
                print(x,y)



    def montre(self, image):
        self.image = image
        cv2.imshow("yo.jpg", self.image)


if __name__ == "__main__":


    
    l_image = "1.jpg"

    img = image()
    image = img.ouverture(l_image)
    img.entree_un_un(image)
    
    img.montre(image)
