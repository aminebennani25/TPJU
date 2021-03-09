

class Compte(object):

    def __init__(self, numCompte, solde):
        self.numCompte = numCompte
        self.solde = solde
        self.nomClient = None

    def getNumCompte(self):
        return self.__getattribute__("numCompte")

    def setNumCompte(self, value):
        self.__setattr__("numCompte", value)

    def getSolde(self):
        return self.__getattribute__("solde")

    def setSolde(self, value):
        self.__setattr__("solde", value)

    def crediter(self, montant):
        if isinstance(montant, (float, int)):
            self.solde += montant
        else:
            raise Exception("TypeError")

    def debiter(self, montant):
        if isinstance(montant, (float, int)):
            if self.solde >= montant:
                self.solde -= montant
            else:
                raise Exception("Account balance is Null")
        else:
            raise Exception("TypeError")

    def getClient(self):
        return self.nomClient
