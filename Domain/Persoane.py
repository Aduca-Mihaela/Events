from Domain.Entitate import Entitate


class Persoana(Entitate):
    def __init__(self, id, nume, adresa):
        super().__init__(id)
        self.__init__nume = nume
        self.__init__adresa = adresa

    #def getIdPersoana(self):
     #   return self.__init__idPersoana

    def getNume(self):
        return self.__init__nume

    def getAdresa(self):
        return self.__init__adresa

    #def setIdPersoana(self, idPersoana):
     #   self.__init__idPersoana = idPersoana

    def setNume(self, nume):
        self.__init__nume = nume

    def setAdresa(self, adresa):
        self.__init__adresa = adresa

    def __str__(self):
        return "Persoana:" + str(self.get_id()) + "\nNume: " + self.getNume() + "\nAdresa: " + self.getAdresa() + "\n"
