from Domain.Entitate import Entitate


class Inscriere(Entitate):
    def __init__(self, id, idPersoana, idEveniment):
        super().__init__(id)
        self.__idPersoana = idPersoana
        self.__idEveniment = idEveniment


    #def getId(self):
     #   return self.__id


    def getIdPersoana(self):
        return self.__idPersoana


    def getIdEveniment(self):
        return self.__idEveniment



    #def setId(self, idNou):
     #   self.__id = idNou


    def setIdPersoana(self, idNouPers):
        self.__idPersoana = idNouPers


    def setIdEveniment(self, idNouEv):
        self.__idEveniment = idNouEv

    def __str__(self):
        # Observati ca dupa ultimul + de la final de rand apare \ -> avem +\
        # inseamna ca vom concatena sirul de caractere in continuare, doar ca acea continuare va fi scrisa pe randul urmator
        return "Inscriere: " + str(self.get_id()) + "\n" +\
                "ID Persoana: " + str(self.getIdPersoana()) + "\n" +\
                "ID Eveniment: " + str(self.getIdEveniment()) + "\n"