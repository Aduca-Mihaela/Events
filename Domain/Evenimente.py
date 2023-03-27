from Domain.Entitate import Entitate


class Evenimente(Entitate):
    def __init__(self, id, data, timp, descriere):
        super().__init__(id)
        self.__init__data = data
        self.__init__timp = timp
        self.__init__descriere = descriere

    #def getIdEveniment(self):
     #   return self.__init__idEveniment

    def getData(self):
        return self.__init__data

    def getTimp(self):
        return self.__init__timp

    def getDescriere(self):
        return self.__init__descriere

    #def setIdEveniment(self, idEveniment):
     #   self.__init__idEveniment = idEveniment

    def setData(self, data):
        self.__init__data = data

    def setTimp(self, timp):
        self.__init__timp = timp

    def setDescriere(self, descriere):
        self.__init__descriere = descriere

    def __str__(self):
        return "Eveniment: " + str(self.get_id()) + "\nDescriere: " + self.getDescriere() + "\nTimp: " + self.getTimp() +"\nData: " + self.getData()+ "\n"