a = 'ajp'

dico = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,
        'g':7,'h':8,'i':9,'j':10,
        'k':11,'l':12, 'm':13,'n':14,'o':15,
        'p':16,'q':17,'r':18,'s':19, 't':20,
        'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}



a = " ".join(a)
a = a.split()
print(a)


journal = []
poids = 1
nb = 1

poidss = 1
ya = True
while ya:
    poidss += 1
    for i in a:
        for cle, valeur in dico.items():
            if i == cle:
                yo = True
                while yo:
                   
                    aa = valeur + poids
             
                    if aa >= 26:
                        journal.append((cle,poids))
                        poids = poidss
                        yo = False
                   

                    
                    
                    poids += 1 

                    
        
        try:
            if journal[-2][1] == 0 and\
               journal[-1][1] == 0 and\
               journal[-3][1] == 0:
                print(nb)
                ya = False
        except:
            pass


    nb += 1
    print(journal)
    



