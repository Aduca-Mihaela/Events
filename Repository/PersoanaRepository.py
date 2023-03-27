class PersoanaRepository:
    def __init__(self):
        self.__persoane = {}


    @property
    def getAll(self):
        '''
        returneaza o lista de persoane
        :return: o lista de obiecte de tipul Persoana
        '''
        return list(self.__persoane.values())

    def getById(self, idPersoana):
        '''
        returneaza persoana cu id-ul dat
        :param idPersoana: string
        :return:un ob de tipul Persoana, daca exista unul cu id-ul dat, altfel None
        '''
        if idPersoana in self.__persoane:
            return self.__persoane[idPersoana]
        return None

    def getByNume(self, nume):
        if nume in self.__persoane:
            return self.__persoane[nume]
        return None

    def adauga(self, persoana):
        '''
        adauga o persoana in dictionar
        :param persoana:ob de tipul persoana
        :return:
        '''
        if self.getById(persoana.get_id()) is not None:
            raise KeyError("Exista deja o persoana cu id-ul dat")
        self.__persoane[persoana.get_id()] = persoana

    def modifica(self, persoanaNoua):
        '''
        modifica o pers dupa id
        :param persoanaNoua:ob de tipul Persoana
        :return:
        '''
        if self.getById(persoanaNoua.get_id()) is None:
            raise KeyError("Nu exista nicio persoana cu id-ul dat")
        self.__persoane[persoanaNoua.get_id()] = persoanaNoua


    def sterge(self, idPersoana):
        '''
        sterge un angajat dupa id
        :param idPersoana:string
        :return:
        '''
        if self.getById(idPersoana) is None:
            raise KeyError("Nu exista niciun angajat cu id-ul dat!")
        self.__persoane.pop(idPersoana)
