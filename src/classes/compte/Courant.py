from .Compte import Compte


class Courant(Compte):

    def __init__(self, numCompte, solde):
        Compte.__init__(self, numCompte, solde)

    def debiter(self, montant: int) -> None:
        if isinstance(montant, (float, int)):
            if self.solde >= montant:
                self.solde -= montant
            else:
                raise Exception("Account balance is Null")
        else:
            raise Exception("TypeError")

    def crediter(self, montant: int) -> None:
        if isinstance(montant, (float, int)):
            self.solde += montant
        else:
            raise Exception("TypeError")
