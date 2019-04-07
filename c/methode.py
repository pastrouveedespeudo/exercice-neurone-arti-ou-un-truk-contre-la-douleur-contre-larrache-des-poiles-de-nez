class ecriture:

    def ecriture0(self, carac, name):
        self.carac = carac
        self.name = name
        
        with open(self.name, "a") as file:
            file.write(str(self.carac))
    
    def ecriture1(self, carac):
        self.carac = carac

        with open("requete.py", "a") as file:

            file.write(self.carac)
            file.write("= [ ")


    def ecriture3(self, carac):
        self.carac = carac

        with open("requete.py", "a") as file:

            file.write()





                       
    def ecriture3(self, carac):
        self.carac = carac

        with open("requete.py", "a") as file:

            file.write(" ]")
                       

class ana:
    def analyse(self):
        pass

















































