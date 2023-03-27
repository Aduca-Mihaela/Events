from Service.EvenimentService import EvenimentService
from Service.InscriereService import InscriereService
from Service.PersoanaService import PersoanaService


class Consola:
    def __init__(self, persoanaService:PersoanaService, evenimentService:EvenimentService, inscriereService:InscriereService):
        self.__persoanaService = persoanaService
        self.__evenimentService = evenimentService
        self.__inscriereService = inscriereService


    def adaugaPersoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei: ")
            nume = input("Dati numele persoanei: ")
            adresa = input("Dati adresa persoanei: ")
            self.__persoanaService.adauga(idPersoana, nume, adresa)
        except KeyError as e:
            print(e)

    def modificaPersoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei de modificat: ")
            numeNou = input("Dati numele nou: ")
            adresaNoua = input("Dati adresa noua: ")
            self.__persoanaService.modifica(idPersoana, numeNou, adresaNoua)
        except KeyError as e:
            print(e)

    def stergePersoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei de sters: ")
            self.__persoanaService.sterge(idPersoana)
        except KeyError as e:
            print(e)

    def adaugaEveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            data = input("Dati data evenimentului: ")
            timp = input("Dati timpul evenimentului : ")
            descriere = input("Dati descrierea evenimentului: ")
            self.__evenimentService.adauga(idEveniment, data, timp, descriere)
        except KeyError as e:
            print(e)

    def modificaEveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului de modificat: ")
            dataNoua = input("Dati data evenimentului nou: ")
            timpNou = input("Dati timpul evenimentului nou : ")
            descriereNoua = input("Dati descrierea evenimentului nou: ")
            self.__evenimentService.modifica(idEveniment, dataNoua, timpNou, descriereNoua)
        except KeyError as e:
            print(e)

    def stergeEveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului de sters: ")
            self.__evenimentService.sterge(idEveniment)
        except KeyError as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def ordoneazaDesc(self):
        #persoana = input("id-ul persoanei:")
        evenimente = self.__inscriereService.ordEvDupaDesc()
        print(evenimente)

    def ordDescData(self):
        evenimente = self.__inscriereService.ordDupaData()
        print(evenimente)

    def ordoneazaEvDupaParticipanti(self):
        rezultat = self.__evenimentService.ordEvenimenteDupaNrParticipanti()
        return rezultat

    def persPartEv(self):
        rezultat = self.__inscriereService.persPartLaCeleMaiMulteEv()

        return rezultat



    def adaugaInsriere(self):
        try:
            id = int(input("Introduceti id:"))
            idPersoana = int(input("Introduceti ID Persoana:"))
            idEveniment = int(input("Introduceti ID Eveniment:"))

            self.__inscriereService.adauga(id, idPersoana, idEveniment)
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def printMeniu(self):
        print("1. Adauga persoana")
        print("2. Modifica persoana")
        print("3. Sterge persoana")
        print("4. Adauga eveniment")
        print("5. Modifica eveniment")
        print("6. Sterge eveniment")
        print("7. Adauga Inscriere Eveniment")
        print("8. Lista de evenimente la care participa o persoana ordonata alfabetic dupa descriere")
        print("9. Lista de evenimente la care participa o persoana ordonata alfabetic dupa data")
        print("10. Primele 20% evenimente cu cei mai multi participanti")
        print("11. Persoanele participante la cele mai multe evenimente")
        print("a1. Afiseaza toate persoanele")
        print("a2. Afiseaza toate evenimentele")
        print("a3. Afiseaza toate inscrierile")
        print("x. Iesire")


    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaPersoana()
            elif optiune == "2":
                self.modificaPersoana()
            elif optiune == "3":
                self.stergePersoana()
            elif optiune == "4":
                self.adaugaEveniment()
            elif optiune == "5":
                self.modificaEveniment()
            elif optiune == "6":
                self.stergeEveniment()
            elif optiune == "7":
                self.adaugaInsriere()
            elif optiune == "8":
                self.ordoneazaDesc()
            elif optiune == "9":
                self.ordDescData()
            elif optiune == "10":
                self.ordoneazaEvDupaParticipanti()
            elif optiune == "11":
                self.persPartEv()
            elif optiune == "a1":
                self.afiseaza(self.__persoanaService.getAllPersoane())
            elif optiune == "a2":
                self.afiseaza(self.__evenimentService.getAllEvenimente())
            elif optiune == "a3":
                self.afiseaza(self.__inscriereService.getAll())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")


