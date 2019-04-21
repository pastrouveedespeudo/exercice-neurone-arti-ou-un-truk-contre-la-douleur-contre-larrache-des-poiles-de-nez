import os

from corps_pika import *
from rond_rouge_pika import *
from yeux_pika import *
import shutil

class main:

    def corps(self):

        os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d\pika')

        liste_image = os.listdir()
        for i in liste_image:
            liste1 = corps_pikachu(i)
            pourcentage = traitement(liste1[0][0], liste1[0][1])
            print(i, pourcentage)


    def sortie_electrique(self):

        os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d\pika')

        liste_image = os.listdir()
        for i in liste_image:
            shutil.move(i, r'C:\Users\jeanbaptiste\Desktop\reso\d')

        os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d')
        for i in liste_image:
                    
            nettoyage_image_outils('rond3.png', 'rond3.png', 0,255,0)
            nettoyage_image_outils('rond2.png', 'rond2.png', 0,255,0)
            nettoyage_image_outils('image_rond_pika.png', 'image_rond_pika.png', 0,255,0)
        
            liste1 = extraction_rose(i)
            liste2 = nettoyage1(liste1[0])
            liste3 = nettoyage2(liste2)
            liste4 = nettoyage3(liste3)
            nettoyage4(liste4)
            contour()
            rond = detection_rond()
            print(rond, i)

        for i in liste_image:
            shutil.move(i, r'C:\Users\jeanbaptiste\Desktop\reso\d\pika')


    def yeux_pika(self):
        
        os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d\pika')

        liste_image = os.listdir()
        for i in liste_image:
            shutil.move(i, r'C:\Users\jeanbaptiste\Desktop\reso\d')

        os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d')
        for image in liste_image:

            nettoyage_image_outils('outils1.png', 'outils1.png', 0,0,255)
            nettoyage_image_outils('outils2.png', 'outils2.png', 0,0,0)
            nettoyage_image_outils('outils3.png', 'outils3.png', 0,0,0)


            yoyo(image)
            yaya()
            liste1 = yuyu()
            yy(image)
            yiyi(liste1)
            pts_autour_yeux(image, liste1)


            path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux"
            os.chdir(path)
            liste = os.listdir()

            c = 0
            for i in liste:
                contour(i, c)
                c+=1


            path = r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux1"
            os.chdir(path)
            liste = os.listdir()

            nb_cercle = 0
            for i in liste:
                cercle = detection_rond(i)
                nb_cercle += cercle

            print(nb_cercle, image)
            
            suppression(r"C:\Users\jeanbaptiste\Desktop\reso\d\yeux1")



            os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d')


            
if __name__ == "__main__":

    main = main()
    #main.corps()
    #main.sortie_electrique()
    main.yeux_pika()
    




































