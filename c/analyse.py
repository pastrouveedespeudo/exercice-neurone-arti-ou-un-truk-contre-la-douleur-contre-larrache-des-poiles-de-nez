import os


A_f = [[],[],[],[],[],[],[],[],[],]

A_m = [[],[],[],[],[],[],[],[],[],]

class analyse:
    def analyse(self):

        traitement = os.listdir()

        liste = []

        liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]
        liste3 = []
        
        for i in traitement:
            if i == "conteneur.py" or i == "input.py"\
               or i == "ligne de route.py" or i == "methode.py"\
               or i == "perso.py" or i == "phrases.py"\
               or i == "texte.py" or i == "traitement.py"\
               or i == "analyse.py" or i == "__pycache__"\
               or i == "requete":
                pass
            else:
                print(i)
                with open(i,"r") as file:
                    liste.append(file.read())

                c = 0
                for i in liste[0]:
                    if i == '\n':
                        c+=1
                    else:
                        liste2[c].append(i)
                

                for i in liste2:
                    if i == []:
                        pass
                    else:
                        liste3.append("".join(i))

                if liste3[1][16] == '1':
                    print("oui")
                    A_f[0].append(liste3[2])
                    A_f[1].append(liste3[3])
                    A_f[2].append(liste3[4])
                    A_f[3].append(liste3[5])
                    A_f[4].append(liste3[6])
                    A_f[5].append(liste3[7])
                    A_f[6].append(liste3[8])
                    A_f[7].append(liste3[9])
                    print(A_f)
                else:
                    A_m[0].append(liste3[2])
                    A_m[1].append(liste3[3])
                    A_m[2].append(liste3[4])
                    A_m[3].append(liste3[5])
                    A_m[4].append(liste3[6])
                    A_m[5].append(liste3[7])
                    A_m[6].append(liste3[8])
                    A_m[7].append(liste3[9])
  
                break
    
    def fonction_a(self):
        pass



if __name__ == "__main__":
    analyse = analyse()
    analyse.analyse()
