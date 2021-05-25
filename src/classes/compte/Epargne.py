from .Compte import Compte


class Epargne(Compte):

    def __init__(self, taux: int, numCompte: int, solde: int):
        Compte.__init__(self, numCompte, solde)
        self.taux = taux

    def setTaux(self, taux: int):
        self.taux = taux

    def getTaux(self) -> int:
        return self.taux

    def calculInterets(self) -> float:
        return self.solde * self.taux / 100

    def getNewSolde(self) -> float:
        self.solde += self.calculInterets()
        return self.solde

    def debiter(self, montant: int):
        pass

    def crediter(self, montant: int):
        pass
