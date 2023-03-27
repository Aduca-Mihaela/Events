class InscriereRepository:

    def __init__(self, persoanaRepository, evenimentRepository):
        self.__listaInscrieri = []

        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def getAll(self):
        return self.__listaInscrieri

    def adauga(self, inscriere):
        id = inscriere.get_id()
        #if self.gasesteInscriereDupaId(id) != -1:
         #   raise KeyError("Inscrierea exista deja!")

        idPersoana = inscriere.getIdPersoana()
        idEveniment = inscriere.getIdEveniment()

        #if self.__persoanaRepository.getById(idPersoana)is None or self.__evenimentRepository.getById(idEveniment) is None:
         #   raise KeyError("Persoana sau Evenimentul inscrierii nu exista!")
        #elif self.gasesteInscriereDupaPersoanaIdsiEvenimentId(idPersoana, idEveniment) != -1:

         #   raise KeyError("Studentul este deja inscris la aceasta disciplina!")
        self.__listaInscrieri.append(inscriere)

    def gasesteInscriereDupaId(self, id):
        '''
        Metoda care gaseste o inscriere in lista de inscrieri, dupa id inscriere
                :param id: id-ul inscrierii cautate
                :return: pozitia unui obiectului de tip inscriere cu id-ul dat in self.__lista_inscrieri;
                        -1 daca nu exista
                '''
        for i in range(0, len(self.__listaInscrieri)):
            inscriere_curenta = self.__listaInscrieri[0]
            if inscriere_curenta.get_id() == id:
                return i
        return -1

    def gasesteInscriereDupaPersoanaIdsiEvenimentId(self, idPersoana, idEveniment):

        for i in range(0, len(self.__listaInscrieri)):
            inscriere_curenta = self.__listaInscrieri[0]
            if inscriere_curenta.getIdPersoana() == idPersoana and inscriere_curenta.getIdEveniment() == idEveniment:
                return i
        return -1

    def existaInscriereEveniment(self, idEveniment):
        for i in range(0, len(self.__listaInscrieri)):
            inscriere_curenta = self.__listaInscrieri[i]
            if inscriere_curenta.getIdEveniment() == idEveniment:
                return True
        return False

