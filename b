from PIL import Image, ImageDraw, ImageChops
import numpy as np
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

        rectangle1 = ""
        rectangle2 = ""

        rectangle_verticale = []
        
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                if (self.image[x,y] == np.array([0,0,0])).all():
                    rectangle_verticale.append((x,y))

        maximum = max(rectangle_verticale)
        minimum = min(rectangle_verticale)

        print(maximum, minimum)
        
        if self.image[minimum[0]:maximum[0], minimum[1]:maximum[1]].all() == np.array([0,0,0]).all():
            print("y'a un rectangle")
            #self.image[7:117, 40:55] = 0,255,0
            retangle1 = True





        cherche_diagonale = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

        c = 0
        
        for y in range(self.image.shape[1]):
            for x in range(self.image.shape[0]):
                if self.image[x,y].all() == np.array([0,0,0]).all():

                    try:
                        cherche_diagonale[c].append((x,y))
          
                    except:
                        pass
                    c+=1


        for i in range(int(round(self.image.shape[1] / 100*50))):
            self.image[cherche_diagonale[-1][0][0]-i, cherche_diagonale[-1][0][1]+i] = 0,255,0
     

        x = 48-i
        y = 9+i

        to_pts = int(round(self.image.shape[1] / 100*130))
        if self.image[x:to_pts,y].all() == np.array([0,0,0]).all():
            print("oui")
        self.image[x:to_pts,y] = 0,255,255



    def barre_du_bas_un(self, image):
        self.image = image


        bas_image = Image.open("2.jpg")

        masque = Image.new('RGB', bas_image.size, color=(255,255,255))

        a = bas_image.size[0]
        b = bas_image.size[1] / 100* 80
        c = 0
        d = bas_image.size[1]

        coords = (a,b, c,d)
   
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(bas_image, masque)

        diff.save("traitement.jpg")


        liste_x_pareil = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

        img = cv2.imread("traitement.jpg")
        liste_y = []

        c = 0
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                
                if img[x,y].all() == np.array([0,0,0]).all():
                    
                    liste_x_pareil.append(x)
                    liste_y.append(y)
                    img[x:,y]
                    if x == x + 1:
                        c+=1

        

        liste_longueur_20_y = []
        liste_longueur_20_y_sur = []
        nos_x = []
        
        c = 0
        for i in liste_y:
            try:
                if liste_y[c+20] - liste_y[c] == 20:
                    liste_longueur_20_y.append((liste_y[c],liste_y[c+20]))
                c+=1
            except:
                pass

        c1 = 0
        try:
            for i in liste_longueur_20_y:
                if img[c1, i[0]:i[1]].all() == np.array([0,0,0]).all():
                    liste_longueur_20_y_sur.append((x,y))
                    nos_x.append(c1)

                else:
                    pass
                c1 += 1
        except:
            pass
        print(nos_x)
        print(liste_longueur_20_y_sur)
        
        img[95:114, 92:110] = 0,0,255
                    


        
        nettoyage_liste = []
        for i in liste_x_pareil:
            if i == []:
                pass
            else:
                nettoyage_liste.append(i)

        print(set(nettoyage_liste))
        img[95]
        cv2.imshow("yo1.jpg", img)
        
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
    img.barre_du_bas_un(l_image)
    
    img.montre(image1)
















    
