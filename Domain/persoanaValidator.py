from Domain.Persoane import Persoana



class PersoanaValidator:
    def valideaza(self, persoana:Persoana):
        erori = []
        if len(persoana.getNume()) < 2:
            erori.append("Numele trebuie sa aiba mai mult de 2 caractere")
        if len(erori) > 0:
            raise Exception(erori)
