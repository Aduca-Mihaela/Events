from Domain.Inscriere import Inscriere


class InscriereService:

    def __init__(self, inscriereRepository, persoanaRepository, evenimentRepository):
        self.__inscriereRepository = inscriereRepository
        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def getAll(self):
        return self.__inscriereRepository.getAll()

    def adauga(self, id, idPersoana, idEveniment):
        inscriere = Inscriere(id, idPersoana, idEveniment)
        self.__inscriereRepository.adauga(inscriere)

    def existaInscriereEveniment(self, idEveniment):
        return self.__inscriereRepository.existaInscriereEveniment(idEveniment)



    def ordoneazaEv(self, idPers):
        idPersoana = self.__persoanaRepository.getById(idPers)
        inscrieri = self.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdPersoana() == idPersoana:
                idEv = inscriere.getIdEveniment()
                ev = self.__evenimentRepository.getById(idEv)
                descriere = ev.getDescriere()
                data = ev.getData()
        lista = sorted()

    def listaEvLaCarePartOPersDupaDescriere(self, idPersoana):
        pers =self.__persoanaRepository.getById(idPersoana)
        inscrieri=self.getAll()
        listaEv = {}
        for inscriere in inscrieri:
            if pers == inscriere.getIdPersoana():
                if inscriere.getIdEveniment() in listaEv:
                    listaEv[inscriere.getIdEveniment] +=1
                else:
                    listaEv[inscriere.getIdEveniment] = 1
        listSort = sorted(listaEv, key=lambda descriere:listaEv[descriere])
        evOrd=[]
        for idEveniment in listSort:
            evOrd.append((idEveniment, listaEv[idEveniment]))
        return evOrd

    def persPartLaCeleMaiMulteEv(self):
        evPers = {}
        inscrieri = self.__inscriereRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdPersoana() in evPers:
                evPers[inscriere.getIdPersoana()] +=1
            else:
                evPers[inscriere.getIdPersoana()] = 1

        idEvOrd = sorted(evPers, key=lambda idEv: evPers[idEv], reverse=True)
        evOrd = []
        numePers = self.__persoanaRepository.getById(inscriere.getIdPersoana())
        for idPersoana in idEvOrd:
            pers = self.__persoanaRepository.getById(inscriere.getIdPersoana())
            evOrd.append((idPersoana, evPers[idPersoana]))


        i=0;
        while(i<len(evOrd)):
            print(evOrd[i])
            i+=1

    def ordEvDupaDesc(self):
        '''
        Metoda ce returneaza studentii de la o disciplina cautata cu notele la acea disciplina, ordonati crescator dupa note, apoi (daca doi studenti au aceeasi nota) dupa numele studentului
        :param nume_disciplina: numele disciplinei cautate
        :return: dictionar sortat dupa note (apoi, in caz de note egale, dupa nume student) cu numele studentilor si notele lor la disciplina cautata
        '''
        lista =[]
        lista2 = []
        idPers = input("Dati id-ul persoanei: ")
        inscrieri = self.getAll()
        for inscriere in inscrieri:
            lista.append(inscriere.getIdPersoana())

        for inscriere in inscrieri:
            i=0
            for idPers in lista:
                if idPers == inscriere.getIdPersoana():
                    if idPers == lista[i]:
                        lista2.append((inscriere.getIdEveniment(),
                                       self.__evenimentRepository.getById(inscriere.getIdEveniment()).getDescriere()))
                        i+=1
                    else:
                        i+=1




        print(lista)
        print(lista2)
        lista2.sort()
        return lista2

    def ordDupaData(self):
        lista = []
        lista2 = []
        idPers = input("Dati id-ul persoanei: ")
        inscrieri = self.getAll()
        for inscriere in inscrieri:
            lista.append(inscriere.getIdPersoana())

        for inscriere in inscrieri:
            i = 0
            for idPers in lista:
                if idPers == inscriere.getIdPersoana():
                    if idPers == lista[i]:
                        lista2.append((inscriere.getIdEveniment(),
                                       self.__evenimentRepository.getById(inscriere.getIdEveniment()).getData()))
                        i += 1
                    else:
                        i += 1

        print(lista)
        print(lista2)
        lista2.sort()
        return lista2













