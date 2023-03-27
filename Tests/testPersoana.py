from Domain.Persoane import Persoana


def testPersoana():
    persoana = Persoana("1", "ana", "Aurel Vlaicu")

    assert persoana.getIdPersoana() == "1"
    assert persoana.getNume() == "ana"
    assert persoana.getAdresa() == "Aurel Vlaicu"

def testPersoanaSetteri():
    persoana = Persoana("1", "ana", "Aurel Vlaicu")

    persoana.setIdPersoana("1")
    assert persoana.getIdPersoana() == "1"

    persoana.setNume("ana")
    assert persoana.getNume() == "ana"

    persoana.setAdresa("Aurel Vlaicu")
    assert persoana.getAdresa() == "Aurel Vlaicu"