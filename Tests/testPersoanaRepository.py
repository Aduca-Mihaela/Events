from Domain.Persoane import Persoana
from Repository.PersoanaRepository import PersoanaRepository


def testAdaugaPersoanaR():
    persRepository = PersoanaRepository()
    persoana = Persoana("1", "ana", "Aurel Vlaicu")

    persRepository.adauga(persoana)

    persoana = persRepository.getAll()
    assert len(persoana) == 1
    assert persoana[0].getIdAngajat() == "1"

    try:
        persRepository.adauga(persoana)
        assert False
    except KeyError:
        ...

def testModificaPersoanaR():
    persRepository = PersoanaRepository()
    persoana = Persoana("1", "ana", "Aurel Vlaicu")
    persoanaN1 = Persoana("2", "marius", "Aurel Vlaicu")
    persoanaN2 = Persoana("3", "vali", "Aurel Vlaicu")
    persRepository.adauga(persoana)

    persoana.modifica(persoanaN1)

    persoane = persRepository.getAll()
    assert persoane[0].getNume() == "marius"

    try:
        persRepository.modifica(persoanaN2)
        assert False
    except KeyError:
        ...

def testStergePersoanaR():
    persRepository = PersoanaRepository()
    persoana = Persoana("1", "ana", "Aurel Vlaicu")
    persRepository.adauga(persoana)

    persRepository.sterge("1")

    assert len(persoana.getAll()) == 0

    try:
        persRepository.sterge("!")
        assert False
    except KeyError:
        ...