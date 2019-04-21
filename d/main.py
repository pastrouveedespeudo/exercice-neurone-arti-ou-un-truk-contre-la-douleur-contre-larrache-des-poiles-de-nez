import os

from corps_pika import *
from rond_rouge_pika import * 
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



        
if __name__ == "__main__":

    main = main()
    #main.corps()
    main.sortie_electrique()






































