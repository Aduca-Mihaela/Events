from Tests.testPersoana import testPersoana, testPersoanaSetteri
from Tests.testPersoanaRepository import testAdaugaPersoanaR, testModificaPersoanaR, testStergePersoanaR


def testAll():
    testPersoana()
    testPersoanaSetteri()

    testAdaugaPersoanaR()
    testModificaPersoanaR()
    testStergePersoanaR()

