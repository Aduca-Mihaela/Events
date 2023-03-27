from Domain.Persoane import Persoana
from Domain.persoanaValidator import PersoanaValidator
from Repository.PersoanaRepository import PersoanaRepository
from Repository.PersoanaRepositoryInFile import PersoanaRepositoryInFile


class PersoanaService:
    def __init__(self, persoanaRepository:PersoanaRepositoryInFile,persoanaValidator:PersoanaValidator):
        self.__persoanaRepository = persoanaRepository
        self.__persoanaValidator = persoanaValidator

    def getAllPersoane(self):
        '''
        returneza o lista de persoane
        :return: lista de ob de tipul Persoana
        '''
        return self.__persoanaRepository.getAll;

    def adauga(self, idPersoana, nume, adresa):
        '''
        adauga un angajat
        :param idPersoana:string
        :param nume: string
        :param adresa: string
        :return:
        '''

        persoana = Persoana(idPersoana, nume, adresa)
        self.__persoanaValidator.valideaza(persoana)
        self.__persoanaRepository.adauga(persoana)

    def modifica(self, idPersoana, numeNou, adresaNoua):
        '''
        modifica o pers dupa id
        :param idPersoana: string
        :param numeNou: string
        :param adresaNoua: string
        :return:
        '''

        persoanaNoua = Persoana(idPersoana, numeNou, adresaNoua)
        self.__persoanaRepository.modifica(persoanaNoua)

    def sterge(self, idPersoana):
        '''
        sterge o pers dupa id
        :param idAngajat: string
        :return:
        '''
        self.__persoanaRepository.sterge(idPersoana)