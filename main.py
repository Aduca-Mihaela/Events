from Domain.Evenimente import Evenimente
from Domain.Inscriere import Inscriere
from Domain.Persoane import Persoana
from Domain.evenimentValidator import EvenimentValidator
from Domain.persoanaValidator import PersoanaValidator
from Repository.EvenimentRepository import EvenimentRepository
from Repository.EvenimentRepositoryInFile import EvenimentRepositoryInFile
from Repository.InscriereRepository import InscriereRepository
from Repository.InscriereRepositoryInFile import InscriereRepositoryInFile
from Repository.PersoanaRepository import PersoanaRepository
from Repository.PersoanaRepositoryInFile import PersoanaRepositoryInFile
from Service.EvenimentService import EvenimentService
from Service.InscriereService import InscriereService
from Service.PersoanaService import PersoanaService
from Tests.testAll import testAll
from UI.Consola import Consola


def main():
    pers1 = Persoana(1, "Maria", "1mai")
    pers2 = Persoana(2, "Mihai", "Aurel Vlaicu")
    pers3 = Persoana(3, "Alex", "dorobanti")


    persoanaRepository = PersoanaRepositoryInFile("persoane.txt")
    evenimentRepository = EvenimentRepositoryInFile("evenimente.txt")
    persoanaValidator = PersoanaValidator()
    evenimentValidator = EvenimentValidator()
    inscriereRepository = InscriereRepositoryInFile("inscrieri.txt", persoanaRepository, evenimentRepository)
    persoanaService = PersoanaService(persoanaRepository, persoanaValidator)
    evenimentService = EvenimentService(evenimentRepository, inscriereRepository, evenimentValidator)
    inscriereService = InscriereService(inscriereRepository, persoanaRepository, evenimentRepository)
    consola = Consola(persoanaService, evenimentService, inscriereService)

    pers1 = Persoana(1, "Maria", "1mai")
    pers2 = Persoana(2, "Mihai", "Aurel Vlaicu")
    pers3 = Persoana(3, "Alex", "dorobanti")
    #persoanaRepository.adauga(pers1)
    #persoanaRepository.adauga(pers2)
    #persoanaRepository.adauga(pers3)

    ev1 = Evenimente(1, str(14.00), str(12.02), "abc")
    ev2 = Evenimente(2, str(18.00), str(14.05), "bal")
    #evenimentRepository.adauga(ev1)
    #evenimentRepository.adauga(ev2)

    insc1 = Inscriere(1, 1, 2)
    insc2 = Inscriere(2, 2, 2)
    insc3 = Inscriere(3, 1, 1)
    #inscriereRepository.adauga(insc1)
    #inscriereRepository.adauga(insc2)
    #inscriereRepository.adauga(insc3)


    consola.meniu()

if __name__ == "__main__":
    main()