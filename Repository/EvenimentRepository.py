class EvenimentRepository:
    def __init__(self):
        self.__evenimente = {}


    @property
    def getAll(self):
        '''
        returneaza lista de evenimente
        :return:o lista de ob de tipul Evenimente
        '''
        return list(self.__evenimente.values())

    def getById(self, idEveniment):
        '''
        returneaza evenimentul cu id-ul dat
        :param idEveniment:string
        :return: un ob de tipul Evenimente daca exista unul cu id-ul dat, altfel None
        '''
        if idEveniment in self.__evenimente:
            return self.__evenimente[idEveniment]
        return None


    def getByDescriere(self, descriere):
        '''
        returneaza evenimentul cu descrierea data
        :param descriere:string
        :return: un ob de tipul Evenimente daca exista unul cu descrierea data, altfel None
        '''
        if descriere in self.__evenimente:
            return self.__evenimente[descriere]
        return None

    def getByData(self, data):
        '''
        returneaza evenimentul cu data data
        :param data:string
        :return: un ob de tipul Evenimente daca exista unul cu data data, altfel None
        '''
        if data in self.__evenimente:
            return self.__evenimente[data]
        return None



    def adauga(self, eveniment):
        '''
        adauga un eveniment in dictionar
        :param eveniment:ob de tipul Evenimente
        :return:
        '''
        if self.getById(eveniment.get_id()) is not None:
            raise KeyError("Exista deja un eveniment cu id-ul dat")
        self.__evenimente[eveniment.get_id()] = eveniment

    def modifica(self, evenimentNou):
       '''
        modifica un eveniment dupa id
       :param evenimentNou:ob de tipul Eveniment
       :return:
       '''
       if self.getById(evenimentNou.getIdEveniment()) is None:
           raise KeyError("Nu exista niciun eveniment cu id-ul dat")
       self.__evenimente[evenimentNou.getIdEveniment()] = evenimentNou

    def sterge(self, idEveniment):
        '''
        sterge un eveniment dupa id
        :param idEveniment:string
        :return:
        '''
        if self.getById(idEveniment) is None:
            raise KeyError("Nu exista niciun angajat cu id-ul dat!")
        self.__evenimente.pop(idEveniment)
