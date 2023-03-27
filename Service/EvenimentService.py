from Domain.Evenimente import Evenimente
from Domain.evenimentValidator import EvenimentValidator
from Repository.EvenimentRepository import EvenimentRepository
from Repository.InscriereRepository import InscriereRepository
from Repository.Repository import Repository


class EvenimentService:
    def __init__(self, evenimentRepository:EvenimentRepository, inscriereRepository:InscriereRepository, evenimentValidator:EvenimentValidator):
        self.__evenimentRepository = evenimentRepository
        self.__inscriereRepository = inscriereRepository
        self.__evenimentValidator = evenimentValidator

    def getAllEvenimente(self):
        '''
        returneaza o lista de evenimente
        :return: lista de ob de tipul Evenimente
        '''
        return self.__evenimentRepository.getAll;

    def adauga(self,idEveniment, data, timp, descriere):
        '''
        adauga un eveniment
        :param idEveniment:string
        :param data: string
        :param timp: string
        :param descriere: string
        :return:
        '''

        eveniment = Evenimente(idEveniment, data, timp, descriere)
        self.__evenimentValidator.valideaza(eveniment)
        self.__evenimentRepository.adauga(eveniment)

    def modifica(self, idEveniment, dataNoua, timpNou, descriereNoua):
        '''
        modifica un eveniment dupa id
        :param idEveniment: string
        :param dataNoua:string
        :param timpNou: string
        :param descriereNoua: string
        :return:
        '''
        evenimentNou = Evenimente(idEveniment, dataNoua, timpNou, descriereNoua)
        self.__evenimentRepository.modifica(evenimentNou)

    def sterge(self, idEveniment):
        '''
        sterge un eveniment dupa id
        :param idEveniment: string
        :return:
        '''
        self.__evenimentRepository.sterge(idEveniment)

    def ordEvenimenteDupaNrParticipanti(self):
        evNrParticipanti = {}
        inscrieri = self.__inscriereRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdEveniment() in evNrParticipanti:
                evNrParticipanti[inscriere.getIdEveniment()] += 1
            else:
                evNrParticipanti[inscriere.getIdEveniment()] = 1

        idEvOrd = sorted(evNrParticipanti,key=lambda idEveniment:(20 / 100)* evNrParticipanti[idEveniment], reverse=True)
        evOrd = []
        ev = self.__evenimentRepository.getById(inscriere.getIdEveniment())
        descriere = ev.getDescriere()
        for idEveniment in idEvOrd :
            evOrd.append((idEveniment, descriere,  evNrParticipanti[idEveniment]))
         #for i in range((20/100)*evNrParticipanti)
        i=0;
        while(i< len(evOrd)*(20/100)):
            print (evOrd[i])
            i+=1





