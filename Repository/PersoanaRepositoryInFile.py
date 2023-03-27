from Domain.Persoane import Persoana
from Repository.PersoanaRepository import PersoanaRepository


class PersoanaRepositoryInFile(PersoanaRepository):
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()

    def adauga(self, persoana):
        super().adauga(persoana)  # cerem metodei adauga din clasa parinte sa adauge disciplina in lista de discipline
        self.scrie_in_fisier()

    def modifica(self, persoana):
        super().modifica(
            persoana)  # cerem metodei adauga din clasa parinte sa modifice disciplina in lista de discipline
        self.scrie_in_fisier()  # aceasta lista modificata noi o salvam in fisier

    def sterge(self, id):
        super().sterge(
            id)  # cerem metodei adauga din clasa parinte sa adauge disciplina cu acel id din lista de discipline
        self.scrie_in_fisier()  # aceasta lista modificata noi o salvam in fisier

    def citeste_din_fisier(self):
        try:
            f = open(self.__nume_fisier, "r")  # deschidem fisierul in modul CITIRE: "read" (de acolo vine "r")
            linie = f.readline().strip("\n")  # citim o prima linie din fisier si scoatem din ea caracterul "\n" (enter)
            while linie != "":  # daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",")  # despartim linia citita folosind separatorul ,
                # lista_atribute va fi o lista ce contine, ca elemente, valorile regasite pe linia curenta
                id = int(lista_atribute[0])  # primul element din lista_atribute e id-ul
                nume = lista_atribute[1]  # al doilea element din lista_atribute e numele disciplinei
                adresa = lista_atribute[2]  # al treilea element din lista_atribute e numele profesorului

                persoana = Persoana(id, nume, adresa)  # cream disciplina folosind valorile citite din fisier
                super().adauga(
                    persoana)  # apelam metoda adauga din clasa parinte (adica din clasa DisciplinaRepository)
                linie = f.readline().strip(
                    "\n")
            f.close()
        except IOError:
            raise IOError(
                "Eroare la deschiderea fisierului " + self.__nume_fisier)  # mesaj de eroare daca nu s-a putut deschide fisierul

    def scrie_in_fisier(self):
        try:
            f = open(self.__nume_fisier, "w")  # deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            listaPers = super().getAll # din lista noastra de discipline, aducem toate disciplinele
            for persoana in listaPers:  # parcurgem fiecare disciplina din lista de discipline
                id = persoana.get_id()
                nume = persoana.getNume()
                adresa = persoana.getAdresa()

                linie = str(
                    id) + "," + nume + "," + adresa + "\n"
                f.write(linie)  # scriem acea linie in fisier
            f.close()  # la final, inchidem fisierul
        except IOError:
            raise IOError(
                "Eroare la deschiderea fisierului " + self.__nume_fisier)